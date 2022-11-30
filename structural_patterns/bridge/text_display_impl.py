#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.bridge.display_impl import DisplayImpl

# ˄


class TextDisplayImpl(DisplayImpl):
    # ˅

    # ˄

    def __init__(self, text):

        # A string to display
        self.__text = text

        # A number of characters in bytes
        self.__width = len(text)

        # ˅
        pass
        # ˄

    def impl_open(self):
        # ˅
        self.__print_line()
        # ˄

    def impl_write(self):
        # ˅
        print(f':{self.__text}:')       # Enclose a text with ":" and display it.
        # ˄

    def impl_close(self):
        # ˅
        self.__print_line()
        # ˄

    def __print_line(self):
        # ˅
        print('*', end='')              # Display "*" mark at the beginning of a frame.
        for _ in range(self.__width):   # Display "." for the number of "width".
            print('.', end='')
        print('*')                      # Display "*" mark at the end of a frame.
        # ˄

    # ˅

    # ˄


# ˅

# ˄
