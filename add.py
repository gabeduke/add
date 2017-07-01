#!/usr/bin/env python3

import argparse
from tinydb import TinyDB


def main(args):

    db = TinyDB('{}.json'.format(args.t))

    if args.c:
        db.purge()
        return

    if args.r:
        for item in db:
            print(item.get('name'))
        return

    for i in args.name:
        db.insert({'name': i})


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument(
        "name", help="List of items", nargs='*'
        )

    parser.add_argument('-c', action='store_true', help='clear the list')

    parser.add_argument('-r', action='store_true', help='read the list')

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-t", action="store",
                        default='default', help='list title')

    args = parser.parse_args()
    main(args)
