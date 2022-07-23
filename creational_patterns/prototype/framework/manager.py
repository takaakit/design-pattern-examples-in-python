#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
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
        d: Display = self.__display[display_name]
        return d.clone()    # Create a new object by asking a concrete class to clone itself. Therefore, do not need to know the concrete Display class name.
        # ˄

    # ˅

    # ˄


# ˅

# ˄
