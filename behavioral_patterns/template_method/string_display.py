#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.template_method.abstract_display import AbstractDisplay

# ˄


class StringDisplay(AbstractDisplay):
    # ˅

    # ˄

    def __init__(self, string):

        self.__string = string

        # String width
        self.__width = len(string)

        # ˅
        pass
        # ˄

    def open(self):
        # ˅
        self.__write_line()      # Write a line
        # ˄

    def write(self):
        # ˅
        print('|' + self.__string + '|')    # Display the character with "|"
        # ˄

    def close(self):
        # ˅
        self.__write_line()      # Write a line
        # ˄

    def __write_line(self):
        # ˅
        print('+', end = '')              # Display an end mark "+"
        for i in range(self.__width):
            print('-', end = '')          # Display a line "-"
        print('+')                        # Display an end mark "+"
        # ˄

    # ˅

    # ˄


# ˅

# ˄
