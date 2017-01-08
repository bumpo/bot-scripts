#!/usr/bin/env python

import json
import os
import subprocess

api = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"

NULL = open(os.devnull, "wb")
out, err = subprocess.Popen(["curl", api], stdout=subprocess.PIPE, stderr=NULL).communicate()

quote = json.loads(out)

print(quote["message"].encode("utf-8"))
