.PHONY: all
all: black lint test coverage

RED=\033[0;31m
YELLOW=\033[0;33m
NC=\033[0m# No Color

PYTHON = Python3

.PHONY = help set up test run clean

help:
	@echo "---------------HELP-----------------"
	@echo "To start testing: type make test"
	@echo "For code-linting: type make lint"
	@echo "To format code style: type make black "
	@echo "To generate coverage: type make coverage"
	@echo "To clean up the folder: type make clean"

.PHONY: black
black:
	${PYTHON} -m black src/

.PHONY: lint
coverage:
	${PYTHON} -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	${PYTHON} -m coverage-badge -o ./data/logo/coverage.svg

.PHONY: test
test:
	${PYTHON} -m pytest --cov-report term-missing --cov=src --verbose --color=yes --ignore=venv

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./docs/build


.PHONY: help Makefile

docs:
	${PYTHON} -m $@  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

