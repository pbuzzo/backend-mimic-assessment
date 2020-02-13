#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string "" is what comes before
the first word in the file.  This will be the seed string.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

__author__ = "Patrick Buzzo"


def create_mimic_dict(filename):
    counter = {}
    last_char = ''
    with open(filename, 'r') as f:
        for line in f:
            single_words = line.split()
            for word in single_words:
                if word[-1] == ",":
                    word = word[:-1]
                if last_char in counter:
                    counter[last_char].append(
                        word.lower())
                else:
                    if last_char:
                        counter[last_char] = [word]
                    elif not last_char:
                        counter[last_char] = [word]
                last_char = word
    mimic_dict = counter
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    new_word_list = []
    values_list = []
    keys = mimic_dict.keys()
    values = mimic_dict.values()
    for i in keys:
        if start_word == i:
            next_list = mimic_dict[i][0]
            # use random.choice() or new build list of values and do
            # radint.random()
            # https://pynative.com/python-random-choice/
            new_word_list.append(random.choice(next_list))
    for i in values:
        values_list.append(i)
        # see tuple manipulation
        # https://www.tutorialspoint.com/python/python_tuples.htm
    while len(new_word_list) < 100:
        new_word_list.append(random.choice(values_list))
    print new_word_list

    """
    Resources:
    https://docs.python.org/2/howto/sorting.html
    https://www.tutorialspoint.com/How-to-iterate-through-a-dictionary-in-Python
    https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/
    https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
    """


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: python mimic.py file-to-read'
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
