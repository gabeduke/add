#!/usr/bin/env python3

import argparse
from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()

def main(args):
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
    parser.add_argument("name", help="List of names (clear or read)", nargs='+')

    args = parser.parse_args()
    main(args)