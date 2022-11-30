#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node

# ˄


# A node corresponding to "program".
class Program(Node):
    # ˅

    # ˄

    def __init__(self):

        self.__command_list = None

        # ˅
        pass
        # ˄

    def parse(self, context):
        # ˅
        # Write here to avoid circular import errors.
        from behavioral_patterns.interpreter.command_list import CommandList

        context.slide_token('program')

        _command_list = CommandList()
        _command_list.parse(context)

        self.__command_list = _command_list     # Hold the parsed command list
        # ˄

    def to_string(self):
        # ˅
        if self.__command_list is not None:
            return f'[program {self.__command_list.to_string()}]'
        else:
            return ''
        # ˄

    # ˅

    # ˄


# ˅

# ˄
