#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-11-13
Purpose: Python find clone
"""

import argparse
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    paths: List[str]
    names: List[str]
    types: List[str]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Python find clone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('paths',
                        metavar='PATH',
                        nargs='+',
                        help='Search paths')

    parser.add_argument('-n',
                        '--name',
                        help='Name',
                        metavar='NAME',
                        nargs='+')

    parser.add_argument('-t',
                        '--type',
                        help='File type',
                        metavar='TYPE',
                        choices=list('fdl'),
                        nargs='+')

    args = parser.parse_args()

    return Args(paths=args.paths, names=args.name, types=args.type)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    def type_filter(entry) -> bool:
        return true

    def name_filter(entry) -> bool:
        return any(map(lambda name: re.search(name, entry), args.names))


    for path in args.paths:
        files = 

# --------------------------------------------------
if __name__ == '__main__':
    main()
