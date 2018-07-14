#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.command.painting_target import PaintingTarget

# ˄


class PaintingCanvas(PaintingTarget):
    # ˅

    # ˄

    def __init__(self, canvas, history):

        self.__painting_color = 'blue'

        # Radius of the painting point
        self.__point_radius = 6.0

        # Painting history
        self.__history = history

        self.__canvas = canvas

        # ˅
        pass
        # ˄

    def paint(self, painting_pos_x, painting_pos_y):
        # ˅
        self.__canvas.create_oval(
            painting_pos_x - self.__point_radius,
            painting_pos_y - self.__point_radius,
            painting_pos_x + self.__point_radius,
            painting_pos_y + self.__point_radius,
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
