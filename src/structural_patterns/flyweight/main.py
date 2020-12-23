#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.flyweight.large_size_string import LargeSizeString

'''
Display a string consisting of large characters. Large character objects are not created until they are needed. And the created objects are reused.
'''

if __name__ == '__main__':
    input_value = input('Please enter digits (ex. 1212123): ')

    bs = LargeSizeString(input_value)
    bs.display()
