#!/usr/bin/env python3.10
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python clone of comm
"""

import argparse
import sys
from typing import NamedTuple, Optional, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file1: TextIO
    file2: TextIO
    show_col1: bool
    show_col2: bool
    show_col3: bool
    insensitive: bool
    delimiter: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python clone of comm',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE')

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE')

    parser.add_argument('-1',
                        '--suppress_col1',
                        help='Suppress column 1',
                        action='store_true')

    parser.add_argument('-2',
                        '--suppress_col2',
                        help='Suppress column 2',
                        action='store_true')

    parser.add_argument('-3',
                        '--suppress_col3',
                        help='Suppress column 3',
                        action='store_true')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive',
                        action='store_true')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output column delimiter',
                        metavar='STR',
                        default='\t')

    args = parser.parse_args()

    if args.file1 == '-' and args.file2 == '-':
        parser.error('Both input files cannot be STDIN ("-")')

    return Args(file1=args.file1,
                file2=args.file2,
                show_col1=not args.suppress_col1,
                show_col2=not args.suppress_col2,
                show_col3=not args.suppress_col3,
                insensitive=args.insensitive,
                delimiter=args.delimiter)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    fh1 = fopen(args.file1)
    fh2 = fopen(args.file2)
    line1 = next_line(fh1)
    line2 = next_line(fh2)

    def printer(text: str, col_num: int) -> None:
        columns = []
        match col_num:
            case(1):
                if args.show_col1:
                    columns.append(text)
            case(2):
                if args.show_col2:
                    if args.show_col1:
                        columns.append("")
                    columns.append(text)
            case(3):
                if args.show_col3:
                    if args.show_col1:
                        columns.append("")
                    if args.show_col2:
                        columns.append("")
                    columns.append(text)
            case(_):
                raise Exception(f'Unknown column "{col_num}"')

        print(args.delimiter.join(columns))

    # while True:
    #     match line1:
    #         (None, None):
    #             break
    #         (val1, None):
    #             printer(val2, 1)
    #             line1 = next_line(fh1)
    #         (None, val2):
    #             printer(line2, 1)
    #             line2 = next_line(fh2)
    #         (val1, val2):
    #             if val1 == val2:
    #                 printer(val1, 3)
    #                 line1 = next_line(fh1)
    #                 line2 = next_line(fh2)
    #             elif val1 < val2:
    #                 printer(val1, 1)
    #                 line1 = next_line(fh1)
    #             else:
    #                 printer(val2, 2)
    #                 line2 = next_line(fh2)

    while line1 is not None or line2 is not None:
        if line1 is not None and line2 is not None:
            if line1 == line2:
                printer(line1, 3)
                line1 = next_line(fh1)
                line2 = next_line(fh2)
            elif line1 < line2:
                printer(line1, 1)
                line1 = next_line(fh1)
            else:
                printer(line2, 2)
                line2 = next_line(fh2)
        elif line1 is not None and line2 is None:
            printer(line1, 1)
            line1 = next_line(fh1)
        else:
            printer(line2, 2)
            line2 = next_line(fh2)


# --------------------------------------------------
def fopen(filename: str) -> TextIO:
    """ Open a file or STDIN """

    return sys.stdin if filename == '-' else open(filename, 'rt')


# --------------------------------------------------
def next_line(fh: TextIO) -> Optional[str]:
    """ Return the next line from a filehandle """

    try:
        return next(fh).rstrip()
    except StopIteration:
        return None


# --------------------------------------------------
if __name__ == '__main__':
    main()
