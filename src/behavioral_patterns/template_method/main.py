#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.template_method.char_display import CharDisplay
from behavioral_patterns.template_method.string_display import StringDisplay

'''
Display a character or string repeatedly 5 times.
'''

if __name__ == '__main__':
    display_1 = CharDisplay('H')
    display_1.output()

    display_2 = StringDisplay('Hello world.')
    display_2.output()
