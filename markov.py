#!/usr/bin/env python
import array
import markovify
import sys
import os.path
import time

args = sys.argv

source_base_path = "/opt/sean/text/"
source_file = os.path.join(source_base_path, "h3.txt")

if len(args) == 2:
    new_source_file = os.path.join(source_base_path, "{0}.txt".format(args[1]))
    if os.path.exists(new_source_file):
        source_file = new_source_file

# Get raw text as string.
with open(source_file) as f:
    text = f.read()

# Build the model.
for i in range(1, 3)[::-1]:

    text_model = markovify.NewlineText(text, state_size=i)
    t = time.time()

    # print a sentence
    # sentence = text_model.make_short_sentence(200, tries=5)
    sentence = text_model.make_sentence()
    if sentence:
        print(sentence)
        break
