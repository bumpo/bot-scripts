#!/usr/bin/env python

import subprocess

m = subprocess.Popen(["mysql", "-N", "-u", "seanconnery", "eggdrop", "-e",  "SELECT `phrase` FROM `mfw-phrases` ORDER BY RAND() limit 1;"], stdout=subprocess.PIPE).communicate()[0]
x = m.strip()
print x
