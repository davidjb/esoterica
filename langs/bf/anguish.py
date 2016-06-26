#!/usr/bin/env python2

from __future__ import print_function
from brainfuck import *


MEM = Memory()
LOOPS = [
    (u"\u200C", MEM.loop),
    (u"\u200D", MEM.endloop),
]
LOOP_CHARS = [LOOPS[0][0], LOOPS[1][0]]
CONTROLLER = {
    u"\u2060": MEM.rshift,
    u"\u200B": MEM.lshift,
    u"\u2061": MEM.inc,
    u"\u2062": MEM.dec,
    u"\u2063": MEM.write,
    u"\uFEFF": MEM.read
}
for key, value in LOOPS:
    CONTROLLER[key] = value


def main(prog):
    if prog["debug"]:
        CONTROLLER[prog["debug"]] = MEM.debug

    prog['code'] = prog['code'].decode('utf-8')
    code = [char for char in prog["code"] if char in CONTROLLER]
    if prog['dump']:
        print("Code output")
        print("-----------")
        print()
        print(u''.join(code))

    loop_chars = (char for char in enumerate(code) if char[1] in LOOP_CHARS)
    MEM.loops = Loops(loop_chars, opener=LOOP_CHARS[0], closer=LOOP_CHARS[1])
    MEM.inpt = (char for char in prog["input"])

    pos = 0
    while pos < len(code):
        pos = CONTROLLER[code[pos]](pos)
    print()


if __name__ == "__main__":
    args = parseArguments()
    main(args)
