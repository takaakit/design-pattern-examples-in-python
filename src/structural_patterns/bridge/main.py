#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.bridge.display import Display
from structural_patterns.bridge.multi_line_display import MultiLineDisplay
from structural_patterns.bridge.text_display_impl import TextDisplayImpl

'''
Display only one line or display the specified number of lines.
'''

if __name__ == '__main__':
    d_1 = Display(TextDisplayImpl('Japan'))
    d_1.output()

    d_2 = MultiLineDisplay(TextDisplayImpl('The United States of America'))
    d_2.output()
    d_2.output_multiple(3)
