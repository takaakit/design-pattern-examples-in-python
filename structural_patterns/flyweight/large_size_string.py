#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.flyweight.large_size_char_factory import LargeSizeCharFactory

# ˄


class LargeSizeString(object):
    # ˅

    # ˄

    def __init__(self, string):

        self.__large_size_chars = []

        # ˅
        for c in list(string):
            self.__large_size_chars.append(LargeSizeCharFactory().get_instance().get_large_size_char(c))
        # ˄

    def display(self):
        # ˅
        for large_size_char in self.__large_size_chars:
            large_size_char.display()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
