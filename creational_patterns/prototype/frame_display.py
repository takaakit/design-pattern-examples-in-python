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

    def clone(self):
        # ˅
        return FrameDisplay(self.__border_char)
        # ˄

    def show(self, message):
        # ˅
        length = len(message)
        print(self.__border_char * (length + 4))
        print(f'{self.__border_char} {message} {self.__border_char}')
        print(self.__border_char * (length + 4))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
