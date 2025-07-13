.PHONY: help
help: ## Prints help for targets with comments
	@cat $(MAKEFILE_LIST) | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: test build pub

.PHONY: req
req: 				## Generate requirements.txt and requirements-dev.txt
	uv export --no-hashes --no-dev -o requirements.txt
	uv export --no-hashes -o requirements-dev.txt

.PHONY: check
check: ## Lint the code using ruff
	uv run ruff check --fix

.PHONY: test
test: tests src 	## Test using pytest
	uv run pytest $^

.PHONY: build
build: test 		## Build a package
	uv build

.PHONY: pub
pub: build			## Publish the package to bsio-pypi
	# uv publish --index bsio-pypi
	uv publish

