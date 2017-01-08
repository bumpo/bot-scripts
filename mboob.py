#!/usr/bin/env python

import subprocess

b = subprocess.Popen(["mysql", "-N", "-u", "seanconnery", "eggdrop", "-e",  "SELECT `phrase` FROM `boobs` ORDER BY RAND() limit 8;"], stdout=subprocess.PIPE).communicate()[0]
for i in b.split("\n"):
	print i
