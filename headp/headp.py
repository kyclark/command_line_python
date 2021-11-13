#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python head clone
"""

import argparse
import sys
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    num_lines: int
    num_bytes: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python head clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin])

    parser.add_argument('-n',
                        '--lines',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-c',
                        '--bytes',
                        help='Number of bytes',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.lines < 1:
        parser.error(f"--lines '{args.lines}' must be > 0")

    if args.bytes is not None and args.bytes < 1:
        parser.error(f"--bytes '{args.bytes}' must be > 0")

    return Args(args.files, args.lines, args.bytes)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    num_files = len(args.files)

    for file_num, fh in enumerate(args.files, start=1):
        if num_files > 1:
            print('{}==> {} <=='.format('\n' if file_num > 1 else '', fh.name))

        if num_bytes := args.num_bytes:
            print(num_bytes)
        else:
            for line_num, line in enumerate(fh, start=1):
                print(line, end='')
                if line_num == args.num_lines:
                    break


# --------------------------------------------------
if __name__ == '__main__':
    main()
