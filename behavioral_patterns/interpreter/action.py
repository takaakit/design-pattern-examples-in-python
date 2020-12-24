#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node

# ˄


# A node corresponding to "forward", "left", and "right".
class Action(Node):
    # ˅

    # ˄

    def __init__(self):

        self.__name = None

        # ˅
        pass
        # ˄

    def parse(self, context):
        # ˅
        self.__name = context.get_token()
        context.slide_token(self.__name)
        if self.__name != 'forward' and self.__name != 'right' and self.__name != 'left':
            exit(str(self.__name) + ' is unknown')
        # ˄

    def to_string(self):
        # ˅
        return str(self.__name)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
