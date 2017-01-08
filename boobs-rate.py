#!/usr/bin/env python

import subprocess
import sys
import time

now = int(time.strftime('%H'))
last = now + 1
try:
	last = open('/opt/sean/boobs.txt').read().splitlines()[0]
	last = int(last)
except:
	pass
if now > last or now < 666:
	b = subprocess.Popen(["mysql", "-N", "-u", "seanconnery", "eggdrop", "-e",  "SELECT `phrase` FROM `boobs` ORDER BY RAND() limit 1;"], stdout=subprocess.PIPE).communicate()[0]
	f = open('/opt/sean/boobs.txt', 'w')
	f.write(str(now));
	f.close();
	print 'boobs ' + b.strip()
else:
	print 'Wait until the next hour.'
