#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.template_method.abstract_display import AbstractDisplay

# ˄


class CharDisplay(AbstractDisplay):
    # ˅

    # ˄

    def __init__(self, char):

        self.__char = char

        # ˅
        pass
        # ˄

    def open(self):
        # ˅
        print('<<', end = '')     # Display "<<" in the start characters.
        # ˄

    def write(self):
        # ˅
        print(self.__char, end = '')  # Display the character.
        # ˄

    def close(self):
        # ˅
        print('>>')             # Display ">>" in the end characters.
        # ˄

    # ˅

    # ˄


# ˅

# ˄
