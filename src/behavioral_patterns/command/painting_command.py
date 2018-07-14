#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.command.command import Command

# ˄


# Command to paint a single point
class PaintingCommand(Command):
    # ˅

    # ˄

    def __init__(self, painting_target, painting_pos_x, painting_pos_y):

        # Painting position x
        self.__painting_pos_x = painting_pos_x

        # Painting position y
        self.__painting_pos_y = painting_pos_y

        self.painting_target = painting_target

        # ˅
        pass
        # ˄

    def execute(self):
        # ˅
        self.painting_target.paint(self.__painting_pos_x, self.__painting_pos_y)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
