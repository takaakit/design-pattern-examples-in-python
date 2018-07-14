#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.decorator.frame import Frame

# ˄


class SideFrame(Frame):
    # ˅

    # ˄

    def __init__(self, display, frame_char):

        # Decoration character
        self.__frame_char = frame_char

        # ˅
        super().__init__(display)
        # ˄

    def get_columns(self):
        # ˅
        return 1 + self.display.get_columns() + 1
        # ˄

    def get_rows(self):
        # ˅
        return self.display.get_rows()
        # ˄

    def get_line_text(self, row):
        # ˅
        return self.__frame_char + self.display.get_line_text(row) + self.__frame_char
        # ˄

    # ˅

    # ˄


# ˅

# ˄
