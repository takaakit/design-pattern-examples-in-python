#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.interpreter.program import Program
from behavioral_patterns.interpreter.context import Context

"""
Analyze the syntax of the mini-language composed of "forward", "left", "right", and "repeat" commands.

-----
Examples before and after syntax analysis.
* Ex.1
Before : "program end"
After  : [program []]

* Ex.2
Before : "program forward right left end"
After  : [program [forward, right, left]]

* Ex.3
Before : "program repeat 4 forward right end end"
After  : [program [[repeat 4 [forward, right]]]]
"""

if __name__ == '__main__':
    with open('./program.txt') as fh:
        for line in fh:
            line = line.strip()
            print('TEXT > \"' + line + '\"')
            node = Program()
            node.parse(Context(line))
            print('NODE > ' + node.to_string())
