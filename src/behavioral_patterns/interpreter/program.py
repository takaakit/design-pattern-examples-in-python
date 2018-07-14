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
        from behavioral_patterns.interpreter.command_list import CommandList
        context.slide_token('program')
        self.__command_list = CommandList()
        self.__command_list.parse(context)
        # ˄

    def to_string(self):
        # ˅
        if self.__command_list is not None:
            return '[program ' + self.__command_list.to_string() + ']'
        else:
            return ''
        # ˄

    # ˅

    # ˄


# ˅

# ˄
