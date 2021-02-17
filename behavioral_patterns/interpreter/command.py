#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.interpreter.node import Node

# ˄


class Command(Node):
    # ˅

    # ˄

    def __init__(self):

        self.__node = None

        # ˅
        pass
        # ˄

    def parse(self, context):
        # ˅
        from behavioral_patterns.interpreter.repeat import Repeat
        from behavioral_patterns.interpreter.action import Action
        _node = None
        if context.get_token() == 'repeat':
            _node = Repeat()
            _node.parse(context)
        else:
            _node = Action()
            _node.parse(context)

        self.__node = _node     # Hold the parsed node
        # ˄

    def to_string(self):
        # ˅
        return self.__node.to_string()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
