""" Tests for headp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './headp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY: str = './tests/inputs/empty.txt'
ONE: str = './tests/inputs/one.txt'
TWO: str = './tests/inputs/two.txt'
THREE: str = './tests/inputs/three.txt'
ELEVEN: str = './tests/inputs/eleven.txt'


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
def test_dies_bad_lines_string() -> None:
    """ Fails on bad number of lines (string) """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} -n {bad} {EMPTY}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"-n/--lines: invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_dies_bad_lines_not_positive() -> None:
    """ Fails on bad number of lines (not positive) """

    bad = random.choice(range(-10, 1))
    rv, out = getstatusoutput(f'{RUN} --lines {bad} {EMPTY}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"--lines '{bad}' must be > 0", out)


# --------------------------------------------------
def test_dies_bad_bytes_string() -> None:
    """ Fails on bad number of bytes (string) """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} -c {bad} {EMPTY}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"-c/--bytes: invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_dies_bad_bytes_not_positive() -> None:
    """ Fails on bad number of bytes (not positive) """

    bad = random.choice(range(-10, 1))
    rv, out = getstatusoutput(f'{RUN} --bytes {bad} {EMPTY}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"--bytes '{bad}' must be > 0", out)


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

    rv, out = getstatusoutput(f'{PRG} {" ".join(args)}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_empty() -> None:
    """ Test with empty """

    run_test([EMPTY], 'tests/expected/empty.txt.out')


# --------------------------------------------------
def test_empty_n2() -> None:
    """ Test with empty """

    run_test(['-n', '2', EMPTY], 'tests/expected/empty.txt.n2.out')


# --------------------------------------------------
def test_empty_n4() -> None:
    """ Test with empty """

    run_test(['-n', '4', EMPTY], 'tests/expected/empty.txt.n4.out')


# --------------------------------------------------
def test_one() -> None:
    """ Test with one """

    run_test([ONE], 'tests/expected/one.txt.out')


# --------------------------------------------------
def test_one_n2() -> None:
    """ Test with one """

    run_test(['-n', '2', ONE], 'tests/expected/one.txt.n2.out')


# --------------------------------------------------
def test_one_n4() -> None:
    """ Test with one """

    run_test(['-n', '4', ONE], 'tests/expected/one.txt.n4.out')


# --------------------------------------------------
def test_eleven() -> None:
    """ Test with eleven """

    run_test([ELEVEN], 'tests/expected/eleven.txt.out')


# --------------------------------------------------
def test_eleven_n2() -> None:
    """ Test with eleven """

    run_test(['-n', '2', ELEVEN], 'tests/expected/eleven.txt.n2.out')


# --------------------------------------------------
def test_eleven_n4() -> None:
    """ Test with eleven """

    run_test(['-n', '4', ELEVEN], 'tests/expected/eleven.txt.n4.out')


# --------------------------------------------------
def test_multiple() -> None:
    """ Test with multiple files """

    run_test([EMPTY, ONE, ELEVEN], 'tests/expected/all.out')


# --------------------------------------------------
def test_multiple_n2() -> None:
    """ Test with multiple files """

    run_test(['-n', '2', EMPTY, ONE, ELEVEN], 'tests/expected/all.n2.out')
