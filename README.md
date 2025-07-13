# [cppwalk](https://github.com/ishbguy/cppwalk)

A C/C++ source code analysis tool powered by clang/libclang.

## Table of Contents

- [:art: Features](#art-features)
- [:straight_ruler: Prerequisite](#straight_ruler-prerequisite)
- [:rocket: Installation](#rocket-installation)
- [:notebook: Usage](#notebook-usage)
- [:memo: Configuration](#memo-configuration)
- [:hibiscus: Contributing](#hibiscus-contributing)
- [:boy: Authors](#boy-authors)
- [:scroll: License](#scroll-license)

## :art: Features

- [ ] Show the whole or a part of the C/C++ AST
- [ ] List the class, method, functuon or other syntax elements
- [ ] Generate call graph, control flow graph

## :straight_ruler: Prerequisite

Ensure that you have installed `clang` package on your system, which provides the `libclang.so` for C/C++ AST manipulation interfaces.

## :rocket: Installation

Use a Python package manager (`pip` and so on) to intall the `cppwalk`, for example:

```sh
pip install cppwalk
```

## :notebook: Usage

```
Usage: cppwalk [OPTIONS] [FILES]...

Options:
  -s, -std, --standard TEXT  specify the C/C++ standard  [default: c++11]
  -I, --include PATH         add include path
  -v, --version              Show the version and exit.
  -h, --help                 Show this message and exit.
```

## :memo: Configuration

TODO.

## :hibiscus: Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## :boy: Authors

- [ishbguy](https://github.com/ishbguy)

## :scroll: License

Released under the terms of [MIT License](./LICENSE).
