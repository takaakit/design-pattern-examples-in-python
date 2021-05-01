#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.command.painting_target import PaintingTarget

# ˄


class PaintingCanvas(PaintingTarget):
    # ˅

    # ˄

    def __init__(self, canvas):

        self.__painting_color = 'blue'

        # Radius of the painting point
        self.__point_radius = 6.0

        self.__canvas = canvas

        # ˅
        pass
        # ˄

    def paint(self, x, y):
        # ˅
        self.__canvas.create_oval(
            x - self.__point_radius,
            y - self.__point_radius,
            x + self.__point_radius,
            y + self.__point_radius,
            fill = self.__painting_color,
            width = 0)
        # ˄

    def clear(self):
        # ˅
        self.__canvas.delete('all')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
