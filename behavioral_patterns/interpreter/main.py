#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from behavioral_patterns.interpreter.program import Program
from behavioral_patterns.interpreter.context import Context

'''
An interpreter for mini language to operate radio controlled car. It parses the following syntax
composed of "forward", "left", "right", and "repeat" commands:
```
<program>      ::= program <command list>
<command list> ::= <command>* end
<command>      ::= <repeat> | <action>
<repeat>       ::= repeat <number> <command list>
<action>       ::= forward | right | left
<number>       ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```
___
Examples before and after syntax analysis.

Ex.1
```
Before parsing : program end
After parsing  : [program []]
```

Ex.2
```
Before parsing : program forward right left end
After parsing  : [program [forward, right, left]]
```

Ex.3
```
Before parsing : program repeat 4 forward right end end
After parsing  : [program [repeat 4 [forward, right]]]
```
'''

if __name__ == '__main__':
    # Reads commands line by line from the "program.txt" and parses them.
    with open(os.path.join(os.path.dirname(__file__), 'program.txt')) as fh:
        for line in fh:
            line = line.strip()
            print(f'Before parsing : {line}')
            node = Program()
            node.parse(Context(line))
            print(f'After parsing  : {node.to_string()}')
