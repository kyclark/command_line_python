#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python clone of uniq
"""

import argparse
import sys
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO
    out_file: TextIO
    show_count: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python clone of uniq',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-c',
                        '--count',
                        help='Show counts',
                        action='store_true')

    args = parser.parse_args()

    return Args(file=args.file, out_file=args.outfile, show_count=args.count)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    def printer(num: int, text: str) -> None:
        if num > 0:
            if args.show_count:
                args.out_file.write(f'{count:>4} {text}')
            else:
                args.out_file.write(text)

    prev = ''
    count = 0
    for line in args.file:
        if line.rstrip() != prev.rstrip():
            printer(count, prev)
            prev = line
            count = 0

        count += 1

    printer(count, prev)


# --------------------------------------------------
if __name__ == '__main__':
    main()
