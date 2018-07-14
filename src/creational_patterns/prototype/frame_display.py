#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.prototype.framework.display import Display

# ˄


class FrameDisplay(Display):
    # ˅

    # ˄

    def __init__(self, border_char):

        self.__border_char = border_char

        # ˅
        pass
        # ˄

    def create_clone(self):
        # ˅
        return FrameDisplay(self.__border_char)
        # ˄

    def show(self, message):
        # ˅
        length = len(message)
        for i in range(length + 4):
            print(self.__border_char, end = '')
        print('')
        print(self.__border_char + ' ' + message + ' ' + self.__border_char)
        for i in range(length + 4):
            print(self.__border_char, end = '')
        print('')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
