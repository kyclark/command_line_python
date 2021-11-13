""" Tests for echop """

import os
from subprocess import run, getstatusoutput
from typing import List

PRG = './echop.py'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage(capsys) -> None:
    """ Prints usage """

    for flag in ['-h', '--help']:
        # rv, out = getstatusoutput(f'{PRG} {flag}')
        # assert rv == 0
        # assert out.lower().startswith('usage')

        res = run([PRG, flag], capture_output=True)
        assert res.returncode == 0
        assert res.stdout.lower().startswith(b'usage')


# --------------------------------------------------
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def run_test(text: List[str], expected_file: str) -> None:
    """ Test with input """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()

    rv, out = getstatusoutput(f'{PRG} {" ".join(text)}')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test_input1() -> None:
    """ Test with input """

    run_test(['Hello there'], './tests/expected/hello1.txt')


# --------------------------------------------------
def test_input2() -> None:
    """ Test with input """

    run_test(['Hello', 'there'], './tests/expected/hello2.txt')


# --------------------------------------------------
def test_input3() -> None:
    """ Test with input """

    run_test(['"Hello  there"', '-n'], './tests/expected/hello1.n.txt')


# --------------------------------------------------
def test_input4() -> None:
    """ Test with input """

    run_test(['-n', 'Hello', 'there'], './tests/expected/hello2.n.txt')
