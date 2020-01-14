package := multihash
sources := $(wildcard $(package)/*.py)

pkg_dirs := build/ dist/ $(package).egg-info/
cache_dirs := __pycache__/ .mypy_cache/

.PHONY += sane check test lint clean-cache clean stub dist publish
.DEFAULT_GOAL := sane

# Sanity checking
sane: lint check test

lint: $(sources)
	-pylint $^
	-flake8 $^

check: $(sources) test.py
	mypy --strict --strict-equality $^

test: test.py
	python $<

# Building and distribution
stub: $(sources)
	stubgen --output . --package $(package)

dist: setup.py sane stub
	python $< sdist bdist_wheel

publish: dist
	twine upload dist/*

# Cleaning
clean-cache:
	rm -rf $(cache_dirs)

clean: setup.py
	python $< clean --all
	rm -rf $(pkg_dirs)
