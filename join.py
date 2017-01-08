#!/usr/bin/env python

import MySQLdb as mdb
import sys

def usage():
    print "Usage: !message requestee message"
    sys.exit(0)

if len(sys.argv) < 3:
    usage()


msg_part = sys.argv[2].split(" ")
if len(msg_part) < 3:
    usage()

requestee = msg_part[1]
msg = " ".join(msg_part[2:])

requestor = sys.argv[1]

try:
    con = mdb.connect("localhost", "seanconnery", "", "eggdrop")

    cur = con.cursor()
    sql = "INSERT INTO join_reminders (requestor, requestee, message) VALUES ('%s', '%s', '%s')"
    cur.execute(sql % (requestor, con.escape_string(requestee), con.escape_string(msg)))
    print "note left"
except mdb.Error, e:
    print "error %d: %s " % (e.args[0], e.args[1])
finally:
    if con:
        con.close()
