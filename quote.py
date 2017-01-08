#!/usr/bin/env python

import subprocess
b = subprocess.Popen(
	[
		"mysql",
		"-N",
		"-u",
		"seanconnery",
		"eggdrop",
		"-e",
		 "SELECT `phrase` FROM `quotes` ORDER BY RAND() limit 1;"
	],
	stdout=subprocess.PIPE
).communicate()[0]
x = b.strip()
print x
