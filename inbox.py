#!/usr/bin/env python

import MySQLdb as mdb
import sys

def usage():
    print "Usage: !inbox user"
    sys.exit(0)

if len(sys.argv) < 3:
    usage()


user = sys.argv[-1].split(" ")[-1]

try:
    con = mdb.connect("localhost", "seanconnery", "", "eggdrop")

    cur = con.cursor()
    sql = "SELECT requestor, message FROM join_reminders WHERE requestee = '%s'"
    cur.execute(sql % con.escape_string(user))
    rows = cur.fetchall()

    if len(rows) == 0:
        print "no messages for {0}".format(user)

    for row in rows:
        msg_from = row[0]
        msg = row[1]
        print "message for {0} from {1}: {2}".format(user, msg_from, msg)

except mdb.Error, e:
    print "error %d: %s " % (e.args[0], e.args[1])
finally:
    if con:
        con.close()
