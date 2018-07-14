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

    def get_columns(self):
        # ˅
        return 1 + self.display.get_columns() + 1
        # ˄

    def get_rows(self):
        # ˅
        return 1 + self.display.get_rows() + 1
        # ˄

    def get_line_text(self, row):
        # ˅
        if row == 0:
            # Upper frame
            return '+' + self.__create_line('-', self.display.get_columns()) + '+'
        elif row == self.display.get_rows() + 1:
            # Bottom frame
            return '+' + self.__create_line('-', self.display.get_columns()) + '+'
        else:
            # Other
            return '|' + self.display.get_line_text(row - 1) + '|'
        # ˄

    def __create_line(self, ch, size):
        # ˅
        buf = []
        for i in range(size):
            buf.append(ch)
        return ''.join(buf)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
