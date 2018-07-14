#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from structural_patterns.flyweight.large_size_string import LargeSizeString

# First, create instances for displaying large size characters, then display large size character string using that instances.

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Usage: python main.py digits')
        print('Ex.  : python main.py 1212123')
    else:
        bs = LargeSizeString(args[1])
        bs.display()
