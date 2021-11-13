#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python cut clone
"""

import argparse
import re
from typing import List, NamedTuple, Optional, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    delimiter: str
    field_pos: List[int]
    byte_pos: List[int]
    char_pos: List[int]


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

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f',
                       '--fields',
                       help='Selected fields',
                       metavar='FIELDS')

    group.add_argument('-b', '--bytes', help='Selected bytes', metavar='BYTES')

    group.add_argument('-c',
                       '--chars',
                       help='Selected characters',
                       metavar='CHARS')

    args = parser.parse_args()

    if not any([args.fields, args.bytes, args.chars]):
        parser.error('Must have --fields, --bytes, or --chars')

    field_pos = None
    byte_pos = None
    char_pos = None

    if args.fields:
        try:
            field_pos = parse_pos(args.fields)
        except Exception as e:
            parser.error(f'Invalid --fields "{args.fields}" ({e})')

    if args.bytes:
        try:
            byte_pos = parse_pos(args.bytes)
        except Exception as e:
            parser.error(f'Invalid --bytes "{args.bytes}" ({e})')

    if args.chars:
        try:
            char_pos = parse_pos(args.chars)
        except Exception as e:
            parser.error(f'Invalid --chars "{args.chars}" ({e})')

    return Args(files=args.files,
                delimiter=args.delim,
                field_pos=field_pos,
                byte_pos=byte_pos,
                char_pos=char_pos)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(args)


# --------------------------------------------------
def parse_pos(text: str) -> List[int]:
    """ Parse a string into a list of ints """

    positions = []
    range_re = re.compile(r'^(\d+)-(\d+)$')

    for val in text.split(','):
        if match := range_re.search(val):
            start = parse_index(match.group(1))
            stop = parse_index(match.group(2))
            if start >= stop:
                raise ValueError(f'First number in range ({start}) '
                                 f'must be lower than second ({stop})')

            positions.extend(list(range(start, stop + 1)))
        else:
            positions.append(parse_index(val))

    return positions


# --------------------------------------------------
def parse_index(text: str) -> int:
    """ Parse an index from a string """

    try:
        if text.startswith('+'):
            raise Exception

        num = int(text)
        if num > 0:
            return num - 1
        else:
            raise Exception
    except Exception:
        raise ValueError(f'Invalid index value "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
