#!/usr/bin/env python
import random
lines = open('/opt/sean/alex.txt').read().splitlines()
myline =random.choice(lines)
print(myline.replace("alex b", "will m")).strip()

