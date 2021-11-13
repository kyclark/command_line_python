#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python cut clone
"""

import argparse
from typing import List, NamedTuple, Optional, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    delimiter: str
    fields: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python cut clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-d',
                        '--delim',
                        help='Field delimiter',
                        metavar='DELIM',
                        default='\t')

    parser.add_argument('-f',
                        '--fields',
                        help='Selected fields',
                        metavar='FIELDS')

    parser.add_argument('-b',
                        '--bytes',
                        help='Selected bytes',
                        metavar='BYTES')

    parser.add_argument('-c',
                        '--chars',
                        help='Selected characters',
                        metavar='CHARS')

    args = parser.parse_args()

    fields = parse_pos(args.fields)

    if not any([args.fields, args.bytes, args.chars]):
        parser.error('Must have --fields, --bytes, or --chars')

    return Args(args.positional, args.arg, args.int, args.file, args.on)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(args)


# --------------------------------------------------
def parse_pos(text: str) -> List[int]:
    """ Parse a string into a list of ints """

    ...


# --------------------------------------------------
def parse_index(text: str) -> Optional[int]:
    """ Parse an index from a string """

    try:
        num = int(text)
        if num > 0:
            return num - 1
    except Exception as e:
        return None


# --------------------------------------------------
def test_parse_index() -> None:
    """ Test parse_index """

    assert parse_index('0') == None
    assert parse_index('1') == 0


# --------------------------------------------------
if __name__ == '__main__':
    main()
