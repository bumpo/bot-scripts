#!/usr/bin/env python

import sys
import random
import MySQLdb as mdb

try:
    con = mdb.connect("localhost", "seanconnery", "", "eggdrop")

    cur = con.cursor()
    cur.execute("SELECT * FROM join_reminders where requestee = '%s'" % sys.argv[1])
    rows = cur.fetchall()

    for row in rows:
        id = row[0]
        msg = "{0}, {1} left a message for you: {2}".format(row[2], row[1], row[3])

        cur.execute("DELETE FROM join_reminders WHERE id = {0}".format(id))
        print msg
    # leave after posting our notes
    if len(rows):
        sys.exit(0)


except mdb.Error, e:
    print "error %d: %s " % (e.args[0], e.args[1])
finally:
    if con:
        con.close()

print random.choice([
        "hi {0}",
        "sup {0}",
        "welcome {0}",
        "heeeeeyyyy, it's {0}! guys, it's {0}!",
        "back for more, {0}?",
        "dude, {0}, whaddup",
        "goddamn it, not {0} again."
    ]).format(sys.argv[1])
