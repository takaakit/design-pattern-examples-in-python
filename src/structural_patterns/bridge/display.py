#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.bridge.display_impl import DisplayImpl

# ˄


class Display(object):
    # ˅

    # ˄

    def __init__(self, impl):

        self.__impl = impl

        # ˅
        pass
        # ˄

    def display(self):
        # ˅
        self.open()
        self.write()
        self.close()
        # ˄

    def open(self):
        # ˅
        self.__impl.impl_open()
        # ˄

    def write(self):
        # ˅
        self.__impl.impl_write()
        # ˄

    def close(self):
        # ˅
        self.__impl.impl_close()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
