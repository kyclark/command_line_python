.PHONY: test

PRG = uniqp.py

test:
	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy $(PRG) tests/test_uniqp.py

all:
	../bin/all_test.py $(PRG)
