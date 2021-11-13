""" Tests for uniqp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './uniqp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY: str = './tests/inputs/empty.txt'
ONE: str = './tests/inputs/one.txt'
TWO: str = './tests/inputs/two.txt'
THREE: str = './tests/inputs/three.txt'
SKIP: str = './tests/inputs/skip.txt'


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

    print(f'{PRG} {" ".join(args)}')
    rv, out = getstatusoutput(f'{PRG} {" ".join(args)}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_empty() -> None:
    """ Test with empty """

    run_test([EMPTY], 'tests/expected/empty.txt.out')


# --------------------------------------------------
def test_empty_c() -> None:
    """ Test with empty """

    run_test(['-c', EMPTY], 'tests/expected/empty.txt.c.out')


# --------------------------------------------------
def test_one() -> None:
    """ Test with one """

    run_test([ONE], 'tests/expected/one.txt.out')


# --------------------------------------------------
def test_one_c() -> None:
    """ Test with one """

    run_test(['-c', ONE], 'tests/expected/one.txt.c.out')


# --------------------------------------------------
def test_two() -> None:
    """ Test with two """

    run_test([TWO], 'tests/expected/two.txt.out')


# --------------------------------------------------
def test_two_c() -> None:
    """ Test with two """

    run_test(['-c', TWO], 'tests/expected/two.txt.c.out')


# --------------------------------------------------
def test_three() -> None:
    """ Test with three """

    run_test([THREE], 'tests/expected/three.txt.out')


# --------------------------------------------------
def test_three_c() -> None:
    """ Test with three """

    run_test(['-c', THREE], 'tests/expected/three.txt.c.out')


# --------------------------------------------------
def test_skip() -> None:
    """ Test with skip """

    run_test([SKIP], 'tests/expected/skip.txt.out')


# --------------------------------------------------
def test_skip_c() -> None:
    """ Test with skip """

    run_test(['-c', SKIP], 'tests/expected/skip.txt.c.out')
