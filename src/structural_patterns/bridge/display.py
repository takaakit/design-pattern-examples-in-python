#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class Display(object):
    # ˅

    # ˄

    def __init__(self, impl):

        self.__impl = impl

        # ˅
        pass
        # ˄

    def output(self):
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
