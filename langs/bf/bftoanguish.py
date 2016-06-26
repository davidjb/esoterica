#!/usr/bin/env python
import sys

CHARMAP = {
    '>': '\u2060',  # WORD JOINER [Cf]
    '<': '\u200B',  # ZERO WIDTH SPACE [Cf]
    '+': '\u2061',  # FUNCTION APPLICATION [Cf]
    '-': '\u2062',  # INVISIBLE TIMES [Cf]
    '.': '\u2063',  # INVISIBLE SEPARATOR [Cf]
    ',': '\uFEFF',  # ZERO WIDTH NO-BREAK SPACE [Cf]
    '[': '\u200C',  # ZERO WIDTH NON-JOINER [Cf]
    ']': '\u200D',  # ZERO WIDTH JOINER [Cf]
}

if __name__ == '__main__':
    if len(sys.argv) == 3:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
            for char, replacement in CHARMAP.items():
                content = content.replace(char, replacement)

        with open(sys.argv[2], 'w', encoding="utf-8") as out:
            out.write(content)
            print('Wrote out to', sys.argv[2])
