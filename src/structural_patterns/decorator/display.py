#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Display(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_columns(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_rows(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_line_text(self, row):
        # ˅
        pass
        # ˄

    # Show all
    def show(self):
        # ˅
        for i in range(self.get_rows()):
            print(self.get_line_text(i))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
