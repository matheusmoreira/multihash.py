package := multihash
sources := $(wildcard $(package)/*.py)
reference_table_url := https://raw.githubusercontent.com/multiformats/multicodec/master/table.csv

pkg_dirs := build/ dist/ $(package).egg-info/
cache_dirs := __pycache__/ .mypy_cache/

.PHONY += sane check check-table test lint clean-cache clean stub dist publish
.DEFAULT_GOAL := sane

# Sanity checking
sane: lint check test

lint: $(sources)
	-pylint $^
	-flake8 $^

check: $(sources) test.py
	mypy --strict --strict-equality $^

check-table: check_table.py
	curl --silent '$(reference_table_url)' | python $<

test: test.py
	python $<

# Building and distribution
stub: $(sources)
	stubgen --output . --package $(package)

dist: setup.py sane check-table stub
	python $< sdist bdist_wheel

publish: dist
	twine upload dist/*

# Cleaning
clean-cache:
	rm -rf $(cache_dirs)

clean: setup.py
	python $< clean --all
	rm -rf $(pkg_dirs)
