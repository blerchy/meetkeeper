#!/usr/local/bin/python3

import sys
import argparse
import os

version = 0.1

description = """Keep track of when2meet.com polls.

Use this tool to register when2meet.com polls that you're in, so you can access them as your schedule changes.

Each poll you register has associated with it an expiry date, usually the last day of the poll. To reduce clutter, the tool removes old polls when the expiry date has passed.

When no arguments are specified, the list of current polls will be printed."""

default_db_file = """version = 0.1
# Meetkeeper database file.
#
# All lines beginning with # are ignored by the tool.
# Valid entries contain first the date in the yyyy-mm-dd format, then a link to the poll. e.g.
# 2020-11-06 https://www.when2meet.com/?example-poll
#
# As polls expire, the tool comments out the lines. As of version 0.1, there is
# no way to change this behaviour, so that lines will be deleted instead.
"""

def main():
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-a", "--add", nargs=2, metavar=("yyyy-mm-dd", "hyperlink"), help="add a new poll to the database, along with expiry date")
    parser.add_argument("-d", "--db-file", nargs=1, metavar="database-filename", help="specify the database file to read/write from. (default: %(default)s)", default="meetkeeper.db")
    parser.add_argument("--version", action="version", version="%(prog)s " + str(version))
    
    args = parser.parse_args()
    db = args.db_file

    if (not os.path.exists(db)):
        print("Notice: database file %s does not exist. Creating new database file at %s" % (db, os.path.abspath(db)))
        with open(db, "w") as f:
            f.write(default_db_file)

    check_version(db)



def check_version(db):
    with open(db, "r") as f:
        for line in f:
            if line.startswith("version"):
                try:
                    db_version = float(line.split()[2])
                    if db_version > version:
                        print("This database file was last used by a more recent version of this tool.\nPlease update the tool to continue using this database file.\n(Exiting to avoid corrupting the database)")
                        sys.exit(1)
                except SystemExit:
                    pass
                except:
                    print("Could not figure out the database file version. Is it corrupted?")
                    sys.exit(1)

if __name__ == "__main__":
    main()

