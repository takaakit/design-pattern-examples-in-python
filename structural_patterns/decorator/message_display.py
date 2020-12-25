#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.decorator.display import Display

# ˄


class MessageDisplay(Display):
    # ˅

    # ˄

    def __init__(self, message):

        # Message to be displayed
        self.__message = message

        # ˅
        super().__init__()
        # ˄

    # Number of characters
    def get_columns(self):
        # ˅
        return len(self.__message)
        # ˄

    # The number of rows is 1
    def get_rows(self):
        # ˅
        return 1
        # ˄

    def get_line_text(self, row):
        # ˅
        if row == 0:
            return self.__message
        else:
            return None
        # ˄

    # ˅

    # ˄


# ˅

# ˄
