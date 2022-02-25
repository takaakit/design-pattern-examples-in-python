#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.prototype.framework.display import Display

# ˄


class UnderlineDisplay(Display):
    # ˅

    # ˄

    def __init__(self, underline_char):

        self.__underline_char = underline_char

        # ˅
        pass
        # ˄

    def clone(self):
        # ˅
        return UnderlineDisplay(self.__underline_char)
        # ˄

    def show(self, message):
        # ˅
        length = len(message)
        print('"' + message + '"')
        print(' ', end='')
        for i in range(length):
            print(self.__underline_char, end='')
        print('')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
