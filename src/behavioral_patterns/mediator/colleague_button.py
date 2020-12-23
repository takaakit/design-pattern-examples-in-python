#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from tkinter import *
from behavioral_patterns.mediator.colleague import Colleague

# ˄


class ColleagueButton(Colleague):
    # ˅

    # ˄

    def __init__(self, button):

        self.__button = button

        # Flag indicating whether the button is pressed
        self.__is_pressed = False

        # ˅
        super().__init__()
        self.__button.bind("<ButtonPress-1>", self.__on_mouse_pressed)
        self.__button.bind("<ButtonRelease-1>", self.__on_mouse_released)
        # ˄

    # Set enable/disable from the Mediator
    def set_activation(self, is_enable):
        # ˅
        if is_enable:
            self.__button.configure(state = NORMAL)
        else:
            self.__button.configure(state = DISABLED)
        # ˄

    def is_pressed(self):
        # ˅
        return self.__button['state'] != DISABLED and self.__is_pressed
        # ˄

    def __on_mouse_pressed(self, event):
        # ˅
        self.__is_pressed = True
        # ˄

    def __on_mouse_released(self, event):
        # ˅
        self.mediator.colleague_changed()
        self.__is_pressed = False
        # ˄

    # ˅

    # ˄


# ˅

# ˄
