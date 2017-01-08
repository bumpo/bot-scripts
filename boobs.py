#!/usr/bin/env python

import subprocess, sys
import random

if len(sys.argv) > 0:
	if random.randint(0,10) >= 9:
		b = subprocess.Popen(["/opt/sean/joelmartinez.py"], stdout=subprocess.PIPE).communicate()[0];
		print b.strip()
		sys.exit(0)
	b = subprocess.Popen(["mysql", "-N", "-u", "seanconnery", "eggdrop", "-e",  "SELECT `phrase` FROM `boobs` ORDER BY RAND() limit 1;"], stdout=subprocess.PIPE).communicate()[0]
	x = b.strip()
	print x
else:
	b = subprocess.Popen(["mysql", "-N", "-u", "seanconnery", "eggdrop", "-e",  "SELECT `phrase` FROM `boobs` WHERE `phrase` LIKE '%nsfw%' ORDER BY RAND() limit 1;"], stdout=subprocess.PIPE).communicate()[0]
	x = b.strip()
	print "boobs " + x

