meetkeeper.py
============

**Keep track of when2meet.com polls.**

If you're popular like me, you may have a few when2meet polls on the go
at any given time. It's hard to keep track of them all, especially if you're
planning things and your availability keeps changing. This tool will help you
keep track of all the polls you're a part of. Add the polls as you join them,
and get a list of them all whenever you need it. The tool will automatically
remove them in the future when they are no longer relevant.

## Usage
```
usage: meetkeeper.py [-h] [-a yyyy-mm-dd hyperlink] [-d database-filename] [--version]

Keep track of when2meet.com polls. Use this tool to register when2meet.com polls that you're in, so
you can access them as your schedule changes. Each poll you register has associated with it an
expiry date, usually the last day of the poll. To reduce clutter, the tool removes old polls when
the expiry date has passed. When no arguments are specified, the list of current polls will be
printed.

optional arguments:
  -h, --help            show this help message and exit
  -a yyyy-mm-dd hyperlink, --add yyyy-mm-dd hyperlink
                        add a new poll to the database, along with expiry date
  -d database-filename, --db-file database-filename
                        specify the database file to read/write from. (default: meetkeeper.db)
  --version             show program's version number and exit
```

