.PHONY: test

test:
	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy echop.py tests/test_echop.py

all:
	../bin/all_test.py echop
