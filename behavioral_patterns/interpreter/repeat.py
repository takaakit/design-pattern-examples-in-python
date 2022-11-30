#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node

# ˄


# A node corresponding to "repeat".
class Repeat(Node):
    # ˅

    # ˄

    def __init__(self):

        self.__number = 0

        self.__command_list = None

        # ˅
        pass
        # ˄

    def parse(self, context):
        # ˅
        # Write here to avoid circular import errors.
        from behavioral_patterns.interpreter.command_list import CommandList

        context.slide_token('repeat')

        self.__number = context.get_number()
        context.slide_token(str(self.__number))

        _command_list = CommandList()
        _command_list.parse(context)

        self.__command_list = _command_list     # Hold the parsed command list
        # ˄

    def to_string(self):
        # ˅
        return f'repeat {self.__number} {self.__command_list.to_string()}'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
