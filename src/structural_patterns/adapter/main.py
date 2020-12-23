#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.adapter.print_message_display import PrintMessageDisplay

'''
Display the given string as follows
```
-- Nice to meet you --
```
or display it as follows.
```
[[ Nice to meet you ]]
```
'''

if __name__ == '__main__':
    p = PrintMessageDisplay('Nice to meet you')
    p.print_weak()
    p.print_strong()
