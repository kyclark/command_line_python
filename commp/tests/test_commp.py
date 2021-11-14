""" Tests for commp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './commp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY: str = './tests/inputs/empty.txt'
FILE1: str = './tests/inputs/file1.txt'
FILE2: str = './tests/inputs/file2.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
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
def test_dies_bad_filename1() -> None:
    """ Fails on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad} {EMPTY}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_dies_bad_filename2() -> None:
    """ Fails on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {EMPTY} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_dies_both_file_stdin() -> None:
    """ Fails on both filenames as '-' """

    rv, out = getstatusoutput(f'{RUN} - -')
    assert rv != 0
    assert re.search('Both input files cannot be STDIN', out)


# --------------------------------------------------
def run_test(args: List[str], expected_file: str) -> None:
    """ Test with input """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()

    print(f'{PRG} {" ".join(args)}')
    rv, out = getstatusoutput(f'{PRG} {" ".join(args)}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_empty_empty() -> None:
    """ Test with empty/empty """

    run_test([EMPTY, EMPTY], 'tests/expected/empty_empty.out')
