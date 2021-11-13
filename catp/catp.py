#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python cat clone
"""

import argparse
import sys
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    number_lines: bool
    number_nonblank_lines: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python cat clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        nargs='+')

    parser.add_argument('-n',
                        '--number_lines',
                        help='Number lines',
                        action='store_true')

    parser.add_argument('-b',
                        '--number_nonblank_lines',
                        help='Number non-blank lines',
                        action='store_true')

    args = parser.parse_args()

    return Args(args.files, args.number_lines, args.number_nonblank_lines)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    for fh in args.files:
        last_num = 0
        for i, line in enumerate(fh, start=1):
            if args.number_lines:
                print(f'{i:6}\t{line}', end='')
            elif args.number_nonblank_lines:
                if line.rstrip():
                    last_num += 1
                    print(f'{last_num:6}\t{line}', end='')
                else:
                    print()
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
