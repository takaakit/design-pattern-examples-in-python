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
        print(f'"{message}"')
        print(f' {self.__underline_char * len(message)}')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
