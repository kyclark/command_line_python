#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python echo clone
"""

import argparse
from typing import List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    text: List[str]
    omit_newline: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python echo clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', nargs='+', help='Text to print')

    parser.add_argument('-n', help='Omit newline', action='store_true')

    args = parser.parse_args()

    return Args(args.text, args.n)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(' '.join(args.text), end='' if args.omit_newline else '\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
