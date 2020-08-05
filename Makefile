PYTHON_CMD := python3
PYTHON_UTEST_CMD := nosetests3
PYTHON_OK := $(shell $(PYTHON_CMD) --version 2>&1)
PYTHON_UTEST_OK := $(shell $(PYTHON_UTEST_CMD) --version 2>&1)
TEST_FILES := $(subst tests/,,$(filter-out $(wildcard tests/**/__init__.py), $(wildcard tests/**/*.py)))
TEST_PACKAGES := $(subst tests/,,$(wildcard tests/*))
TESTS := $(TEST_PACKAGES) $(TEST_FILES)

ifeq ('$(PYTHON_OK)','')
$(error The '$(PYTHON_CMD)' package is not installed.)
endif

ifeq ('$(PYTHON_UTEST_OK)','')
$(error The '$(PYTHON_UTEST_CMD)' package is not installed.)
endif

.PHONY: env docs preview deps write-deps list-tests test-all package clean

env:
	virtualenv .env

docs:
	sphinx-apidoc -o docs/ src/*
	make -C $(PWD)/docs html

preview:
	$(PYTHON_CMD) -m http.server --directory $(PWD)/docs/_build/html

deps:
	pip install -r requirements.txt

write-deps:
	pip freeze > requirements.txt

list-tests:
	@printf "%s\n" $(foreach test,$(TESTS),$(test))

$(TESTS):
	$(PYTHON_UTEST_CMD) tests/$@

test-all: $(TEST_PACKAGES)

package:
	$(PYTHON_CMD) setup.py sdist bdist_wheel

clean:
	rm -rf docs/_build/*
