#!/usr/bin/env python

import sys
import random

print random.choice([
        "bye {0}",
        "later {0}",
        "come back soon {0}",
        "awww man, {0} left, I love {0}!",
        "finally! I've been waiting for {0} to leave for forever!",
        "geez, {0}, ragequit much?",
        "lol, {0} just can't take it!"
    ]).format(sys.argv[1])
