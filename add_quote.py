#!/usr/bin/env python

import MySQLdb as mdb
import sys

con = None

table = "quotes"
item = " ".join(sys.argv)
aq_pos = item.find("!aq")
if aq_pos == -1:
    print "no quote?"
    sys.exit(0)
item = item[aq_pos + 2:]
try:
	con = mdb.connect('localhost', 'seanconnery', '', 'eggdrop')

	cur = con.cursor()
	cur.execute("INSERT INTO " + table + " (phrase) VALUES (%s)", (item))
	print "quote added"
except mdb.Error, e:
	print "error %d: %s " % (e.args[0], e.args[1])

finally:
	if con:
		con.close()
