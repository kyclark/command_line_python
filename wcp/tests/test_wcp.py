""" Tests for wcp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import List

PRG: str = './wcp.py'
RUN: str = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY: str = './tests/inputs/empty.txt'
FOX: str = './tests/inputs/fox.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_dies_bad_file() -> None:
    """ Dies on bad filename """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
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
    """ Test on empty """

    run_test([EMPTY], './tests/expected/empty.txt.out')


# --------------------------------------------------
def test_empty_l() -> None:
    """ Test on empty """

    run_test(['-l', EMPTY], './tests/expected/empty.txt.l.out')


# --------------------------------------------------
def test_empty_w() -> None:
    """ Test on empty """

    run_test(['-w', EMPTY], './tests/expected/empty.txt.w.out')


# --------------------------------------------------
def test_empty_c() -> None:
    """ Test on empty """

    run_test(['-c', EMPTY], './tests/expected/empty.txt.c.out')


# --------------------------------------------------
def test_empty_m() -> None:
    """ Test on empty """

    run_test(['-m', EMPTY], './tests/expected/empty.txt.m.out')


# --------------------------------------------------
def test_empty_wc() -> None:
    """ Test on empty """

    run_test(['-wc', EMPTY], './tests/expected/empty.txt.wc.out')


# --------------------------------------------------
def test_empty_wm() -> None:
    """ Test on empty """

    run_test(['-wm', EMPTY], './tests/expected/empty.txt.wm.out')


# --------------------------------------------------
def test_empty_wl() -> None:
    """ Test on empty """

    run_test(['-wl', EMPTY], './tests/expected/empty.txt.wl.out')


# --------------------------------------------------
def test_empty_cl() -> None:
    """ Test on empty """

    run_test(['-cl', EMPTY], './tests/expected/empty.txt.cl.out')


# --------------------------------------------------
def test_empty_ml() -> None:
    """ Test on empty """

    run_test(['-ml', EMPTY], './tests/expected/empty.txt.ml.out')


# --------------------------------------------------
def test_empty_lwm() -> None:
    """ Test on empty """

    run_test(['-lwm', EMPTY], './tests/expected/empty.txt.lwm.out')


# --------------------------------------------------
def test_fox() -> None:
    """ Test on fox """

    run_test([FOX], './tests/expected/fox.txt.out')


# --------------------------------------------------
def test_fox_l() -> None:
    """ Test on fox """

    run_test(['-l', FOX], './tests/expected/fox.txt.l.out')


# --------------------------------------------------
def test_fox_w() -> None:
    """ Test on fox """

    run_test(['-w', FOX], './tests/expected/fox.txt.w.out')


# --------------------------------------------------
def test_fox_c() -> None:
    """ Test on fox """

    run_test(['-c', FOX], './tests/expected/fox.txt.c.out')


# --------------------------------------------------
def test_fox_m() -> None:
    """ Test on fox """

    run_test(['-m', FOX], './tests/expected/fox.txt.m.out')


# --------------------------------------------------
def test_fox_wc() -> None:
    """ Test on fox """

    run_test(['-wc', FOX], './tests/expected/fox.txt.wc.out')


# --------------------------------------------------
def test_fox_wm() -> None:
    """ Test on fox """

    run_test(['-wm', FOX], './tests/expected/fox.txt.wm.out')


# --------------------------------------------------
def test_fox_wl() -> None:
    """ Test on fox """

    run_test(['-wl', FOX], './tests/expected/fox.txt.wl.out')


# --------------------------------------------------
def test_fox_cl() -> None:
    """ Test on fox """

    run_test(['-cl', FOX], './tests/expected/fox.txt.cl.out')


# --------------------------------------------------
def test_fox_ml() -> None:
    """ Test on fox """

    run_test(['-ml', FOX], './tests/expected/fox.txt.ml.out')


# --------------------------------------------------
def test_fox_lwm() -> None:
    """ Test on fox """

    run_test(['-lwm', FOX], './tests/expected/fox.txt.lwm.out')


# # --------------------------------------------------
# def test_one():
#     """Test on one"""

#     rv, out = getstatusoutput(f'{PRG} {one_line}')
#     assert rv == 0
#     assert out.rstrip() == '       1       1       2 ./inputs/one.txt'

# # --------------------------------------------------
# def test_two():
#     """Test on two"""

#     rv, out = getstatusoutput(f'{PRG} {two_lines}')
#     assert rv == 0
#     assert out.rstrip() == '       2       2       4 ./inputs/two.txt'

# # --------------------------------------------------
# def test_fox():
#     """Test on fox"""

#     rv, out = getstatusoutput(f'{PRG} {fox}')
#     assert rv == 0
#     assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'

# # --------------------------------------------------
# def test_more():
#     """Test on more than one file"""

#     rv, out = getstatusoutput(f'{PRG} {fox} {sonnet}')
#     expected = ('       1       9      45 ../inputs/fox.txt\n'
#                 '      17     118     661 ../inputs/sonnet-29.txt\n'
#                 '      18     127     706 total')
#     assert rv == 0
#     assert out.rstrip() == expected

# # --------------------------------------------------
# def test_stdin():
#     """Test on stdin"""

#     rv, out = getstatusoutput(f'{PRG} < {fox}')
#     assert rv == 0
#     assert out.rstrip() == '       1       9      45 <stdin>'
