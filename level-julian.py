#!/usr/bin/python

import random
import sys

el1, el2 = None, None
if len(sys.argv) == 2 and sys.argv[1].index("/") != -1:
    els = sys.argv[1].split("/")
    el1 = els[0]
    el2 = els[1]
elif len(sys.argv) == 4:
    el1 = sys.argv[1]
    el2 = sys.argv[3]

def genLines():
    total_length = 15
    idx = random.randint(0, total_length)
    lines = ""
    for i in range(0, total_length):
        if idx == i:
            lines += "[X]"
        else:
            lines += "-"
    return lines

print "{0} |{1}| {2}".format(el1, genLines(), el2)
