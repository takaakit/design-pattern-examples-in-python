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
        current_token = context.get_token()
        if current_token != 'forward' and current_token != 'right' and current_token != 'left':
            exit(f'ERROR: {current_token} is unknown')

        self.__name = current_token     # Hold the current token as this action name

        context.slide_token(token=current_token)
        # ˄

    def to_string(self):
        # ˅
        return str(self.__name)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
