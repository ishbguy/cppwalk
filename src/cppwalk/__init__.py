import clang.cindex
from clang.cindex import CursorKind, TypeKind
import click

# 配置Clang库路径（需替换为本地路径）
# clang.cindex.Config.set_library_path("/usr/lib/llvm-14/lib")

def get_function_prototype(cursor):
    """获取函数或方法的完整原型"""
    # 获取函数名称
    class_name = cursor.semantic_parent.spelling if cursor.semantic_parent else ""
    func_name = cursor.spelling or cursor.displayname

    # 获取返回类型
    return_type = cursor.result_type.spelling if cursor.result_type.kind != TypeKind.INVALID else "void"

    # 获取参数列表
    params = []
    for child in cursor.get_children():
        if child.kind == CursorKind.PARM_DECL:
            param_type = child.type.spelling
            param_name = child.spelling or ""
            params.append(f"{param_type} {param_name}")

    # 构造函数原型
    params_str = ", ".join(params)
    return f"{return_type} {class_name}::{func_name}({params_str})"

def print_cpp_entities(file_path, compile_args=None):
    """解析C++文件并打印类、方法、函数信息"""
    if compile_args is None:
        compile_args = ['-std=c++17', '-I/usr/include/c++/11']
    
    index = clang.cindex.Index.create()
    tu = index.parse(file_path, args=compile_args)
    root = tu.cursor

    for node in root.walk_preorder():
        """递归遍历AST节点"""
        # 类定义（含结构体/联合体）
        if node.kind == CursorKind.CLASS_DECL and node.is_definition:
            print(f"[Class] {node.spelling} (LOC: {node.location})")
        
        elif node.kind == CursorKind.STRUCT_DECL and node.is_definition:
            print(f"[Struct] {node.spelling} (LOC: {node.location})")

        elif node.kind == CursorKind.UNION_DECL and node.is_definition:
            print(f"[Union] {node.spelling} (LOC: {node.location})")

        # 成员函数定义
        elif node.kind == CursorKind.CXX_METHOD and node.is_definition():
            # 获取类名
            class_name = node.semantic_parent.spelling if node.semantic_parent else "UnknownClass"

            # 获取方法原型
            method_prototype = get_function_prototype(node)

            # 添加限定符信息
            const_str = " const" if node.is_const_method() else ""
            static_str = "static " if node.is_static_method() else ""
            virtual_str = "virtual " if node.is_virtual_method() else ""

            full_prototype = f"{virtual_str}{static_str}{method_prototype}{const_str}"
            print(f"  [Method] {node.spelling} <{full_prototype}> (LOC: {node.location})")
            # 打印函数体源码
            # with open(file_path, 'r') as f:
            #     source = f.read()[node.extent.start.offset:node.extent.end.offset]
            #     print(f"    ```cpp\n{source}\n    ```")
        
        # 普通函数定义
        elif node.kind == CursorKind.FUNCTION_DECL and node.is_definition():
            # if node.location.file and node.location.file.name == file_path:
            prototype = get_function_prototype(node)
            print(f"[Function] {node.spelling} <{prototype}> (LOC: {node.location})")

@click.command(context_settings=dict(help_option_names=['-h', '--help']),
               epilog='See https://github.com/ishbguy/cppwalk for more details. The program is released under the terms of MIT license.')
@click.option('-s', '-std', '--standard', default='c++11', show_default=True, help='specify the C/C++ standard')
@click.option('-I', '--include', envvar='INC_PATH', multiple=True, type=click.Path(), help='add include path')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.version_option(None, '-v', '--version')
def main(standard: str, include: tuple[str, ...], files: tuple[str, ...]) -> None:
    inc_paths=[ f"-I{inc}" for inc in include ]
    for file in files:
        print_cpp_entities(file, compile_args=[f"-std={standard}", f"{' '.join(inc_paths)}"])

