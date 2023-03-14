#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.decorator.frame import Frame

# ˄


class FullFrame(Frame):
    # ˅

    # ˄

    def __init__(self, display):
        # ˅
        super().__init__(display)
        # ˄

    # Number of characters added left and right decoration characters
    def get_columns(self):
        # ˅
        return 1 + self.display.get_columns() + 1
        # ˄

    # Number of rows added the upper and lower decoration lines
    def get_rows(self):
        # ˅
        return 1 + self.display.get_rows() + 1
        # ˄

    def get_line_text(self, row):
        # ˅
        if row == 0:
            return '+' + self.__create_line('-', self.display.get_columns()) + '+'  # Upper frame
        elif row == self.display.get_rows() + 1:
            return '+' + self.__create_line('-', self.display.get_columns()) + '+'  # Bottom frame
        else:
            return '|' + self.display.get_line_text(row=row - 1) + '|'              # Other
        # ˄

    def __create_line(self, ch, size):
        # ˅
        return ch * size
        # ˄

    # ˅

    # ˄


# ˅

# ˄
