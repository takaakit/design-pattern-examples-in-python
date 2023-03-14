#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node

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
        # Write here to avoid circular import errors.
        from behavioral_patterns.interpreter.command import Command

        while True:
            if context.get_token() is None:
                exit('ERROR: Missing \'end\'')
            elif context.get_token() == 'end':
                context.slide_token(token='end')
                break
            else:
                _node = Command()
                _node.parse(context)

                self.__nodes.append(_node.to_string())   # Hold the parsed node
        # ˄

    def to_string(self):
        # ˅
        return f'[{", ".join(self.__nodes)}]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
