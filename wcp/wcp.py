#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python wc clone
"""

import argparse
import io
import operator
import sys
import platform
import os
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    show_lines: bool
    show_words: bool
    show_bytes: bool
    show_chars: bool


class FileInfo(NamedTuple):
    """ Counts from a file """
    num_lines: int
    num_words: int
    num_bytes: int
    num_chars: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python wc clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file(s)',
                        nargs='*',
                        default=[sys.stdin])

    parser.add_argument('-w',
                        '--words',
                        help='Show word count',
                        action='store_true')

    parser.add_argument('-c',
                        '--bytes',
                        help='Show byte count',
                        action='store_true')

    parser.add_argument('-m',
                        '--chars',
                        help='Show character count',
                        action='store_true')

    parser.add_argument('-l',
                        '--lines',
                        help='Show line count',
                        action='store_true')

    args = parser.parse_args()

    if all(map(operator.not_,
               [args.lines, args.words, args.bytes, args.chars])):
        args.lines = True
        args.words = True
        args.bytes = True

    return Args(files=args.files,
                show_lines=args.lines,
                show_words=args.words,
                show_bytes=args.bytes,
                show_chars=args.chars)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """
    if platform.system() == 'Darwin':
        os.system('say "jazz noise"')

    args = get_args()

    total_lines, total_words, total_bytes, total_chars = 0, 0, 0, 0
    for fh in args.files:
        info = count(fh)
        total_lines += info.num_lines
        total_words += info.num_words
        total_bytes += info.num_bytes
        total_chars += info.num_chars

        print('{}{}{}{}{}'.format(
            format_field(info.num_lines, args.show_lines),
            format_field(info.num_words, args.show_words),
            format_field(info.num_bytes, args.show_bytes),
            format_field(info.num_chars, args.show_chars),
            f' {fh.name}' if fh != sys.stdin else ''))

    if len(args.files) > 1:
        print('{}{}{}{} total'.format(
            format_field(total_lines, args.show_lines),
            format_field(total_words, args.show_words),
            format_field(total_bytes, args.show_bytes),
            format_field(total_chars, args.show_chars)))


# --------------------------------------------------
def count(fh: TextIO) -> FileInfo:
    """ Count the elements in a file """

    num_lines, num_words, num_bytes, num_chars = 0, 0, 0, 0
    for line in fh:
        num_lines += 1
        num_bytes += len(line)
        num_chars += len(line)  # TODO: fix
        num_words += len(line.split())

    return FileInfo(num_lines=num_lines,
                    num_words=num_words,
                    num_bytes=num_bytes,
                    num_chars=num_chars)


# --------------------------------------------------
def test_count() -> None:
    """ Test count """

    assert count(io.StringIO('')) == FileInfo(num_lines=0,
                                              num_words=0,
                                              num_bytes=0,
                                              num_chars=0)

    text = 'The quick brown fox jumps over the lazy dog.\n'
    assert count(io.StringIO(text)) == FileInfo(num_lines=1,
                                                num_words=9,
                                                num_bytes=45,
                                                num_chars=45)


# --------------------------------------------------
def format_field(val: int, show: bool) -> str:
    """ Format a field """

    return f'{val:>8}' if show else ""


# --------------------------------------------------
if __name__ == '__main__':
    main()
