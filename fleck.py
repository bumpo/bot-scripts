#!/usr/bin/env python

import sys

message = " ".join(sys.argv[1:])
message = message.replace("fuck", "fleck")
message = message.replace("FUCK", "FLECK")

new_message = "Excuse me, I think you meant: {0}".format(message)
print(new_message)
