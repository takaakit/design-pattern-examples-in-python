#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node
from behavioral_patterns.interpreter.command import Command

# ˄


class CommandList(Node):
    # ˅

    # ˄

    def __init__(self):

        self.__nodes = []

        # ˅
        pass
        # ˄

    def parse(self, context):
        # ˅
        while True:
            if context.get_token() is None:
                exit('Missing \'end\'')
            elif context.get_token() == 'end':
                context.slide_token('end')
                break
            else:
                commandNode = Command()
                commandNode.parse(context)
                self.__nodes.append(commandNode.to_string())
        # ˄

    def to_string(self):
        # ˅
        return ', '.join(self.__nodes)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
