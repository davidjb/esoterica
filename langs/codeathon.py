#!/usr/bin/env python3
import sys
import datetime
import os


def coding():
    print(datetime.datetime.now().year)

def our():
    print('Goodbye')

def null():
    pass

def delete():
    os.unlink(sys.argv[1])

LANGUAGE = {
    'C': coding,
    'o': our,
    'd': delete,
    'e': everything,
    'a': aaand,
    't': thats,
    'h': ,
    'n': 8,
    '0': null,
    '1': null,
    '2': null,
    '6': null,
    '!': 
}


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        code = f.read().strip()
    lang = LANGUAGE
    for char in code:
        if char in lang:
            lang[char]()
