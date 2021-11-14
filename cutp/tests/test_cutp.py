""" Tests for cutp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './cutp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
CSV: str = 'tests/inputs/movies1.csv'
TSV: str = 'tests/inputs/movies1.tsv'
BOOKS: str = 'tests/inputs/books.tsv'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage(capsys) -> None:
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_dies_bad_filename() -> None:
    """ Fails on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run_test(args: List[str], expected_file: str) -> None:
    """ Test with input """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()

    rv, out = getstatusoutput(f'{RUN} {" ".join(args)}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_movies_tsv_f1() -> None:
    """ Test with movies1.tsv """

    run_test([TSV, '-f', '1'], 'tests/expected/movies1.tsv.f1.out')


# --------------------------------------------------
def test_movies_csv_f1() -> None:
    """ Test with movies.csv """

    run_test([CSV, '-d', ',', '-f', '1'],
             'tests/expected/movies1.csv.f1.dcomma.out')
