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
        if context.get_token() == 'repeat':
            self.__node = Repeat()
        else:
            self.__node = Action()
        self.__node.parse(context)
        # ˄

    def to_string(self):
        # ˅
        return self.__node.to_string()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
