""" Tests for catp """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './catp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY: str = './tests/inputs/empty.txt'
FOX: str = 'tests/inputs/fox.txt'
SPIDERS: str = 'tests/inputs/spiders.txt'
BUSTLE: str = 'tests/inputs/bustle.txt'


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
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage')


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_input() -> None:
    """ Fails on bad input """

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
def test_empty_n() -> None:
    """ Test with empty -n """

    run_test([EMPTY, '-n'], 'tests/expected/empty.txt.n.out')


# --------------------------------------------------
def test_empty_b() -> None:
    """ Test with empty -b """

    run_test([EMPTY, '-b'], 'tests/expected/empty.txt.b.out')


# --------------------------------------------------
def test_fox() -> None:
    """ Test with fox """

    run_test([FOX], 'tests/expected/fox.txt.out')


# --------------------------------------------------
def test_fox_n() -> None:
    """ Test with fox -n """

    run_test([FOX, '-n'], 'tests/expected/fox.txt.n.out')


# --------------------------------------------------
def test_fox_b() -> None:
    """ Test with fox -b """

    run_test([FOX, '-b'], 'tests/expected/fox.txt.b.out')


# --------------------------------------------------
def test_spiders() -> None:
    """ Test with spiders """

    run_test([SPIDERS], 'tests/expected/spiders.txt.out')


# --------------------------------------------------
def test_spiders_n() -> None:
    """ Test with spiders -n """

    run_test([SPIDERS, '-n'], 'tests/expected/spiders.txt.n.out')


# --------------------------------------------------
def test_spiders_b() -> None:
    """ Test with spiders -b """

    run_test([SPIDERS, '-b'], 'tests/expected/spiders.txt.b.out')


# --------------------------------------------------
def test_bustle() -> None:
    """ Test with bustle """

    run_test([BUSTLE], 'tests/expected/bustle.txt.out')


# --------------------------------------------------
def test_bustle_n() -> None:
    """ Test with bustle -n """

    run_test([BUSTLE, '-n'], 'tests/expected/bustle.txt.n.out')


# --------------------------------------------------
def test_bustle_b() -> None:
    """ Test with bustle -b """

    run_test([BUSTLE, '-b'], 'tests/expected/bustle.txt.b.out')
