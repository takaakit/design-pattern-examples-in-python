#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import copy
from creational_patterns.prototype.framework.display import Display

# ˄


class Manager(object):
    # ˅

    # ˄

    def __init__(self):

        self.__display = {}

        # ˅
        pass
        # ˄

    def register_display(self, display_name, display):
        # ˅
        self.__display[display_name] = display
        # ˄

    def get_display(self, display_name):
        # ˅
        d = self.__display[display_name]
        return copy.deepcopy(d)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
