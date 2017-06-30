#!/usr/bin/env python3

import argparse
from tinydb import TinyDB


def main(args):

    if not args.db:
        db = TinyDB('db.json')
    else:
        db = TinyDB('{}.json'.format(args.db))

    if "clear" in args.name:
        db.purge()
        return

    if "read" in args.name:
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
        "name", help="List of names (clear or read)", nargs='+'
        )

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-db", "--database", action="store", dest="db")

    args = parser.parse_args()
    main(args)
