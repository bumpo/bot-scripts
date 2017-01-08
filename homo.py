#!/usr/bin/env python
import random
lines = open('/opt/sean/homs.txt').read().splitlines()
myline =random.choice(lines)
print(myline).strip()
