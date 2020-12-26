#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from tkinter import *
from behavioral_patterns.mediator.colleague import Colleague

# ˄


class ColleagueTextField(Colleague):
    # ˅

    # ˄

    def __init__(self, text_field):

        # Flag indicating whether the text is empty
        self.__is_empty = True

        self.__text_field = text_field

        # ˅
        super().__init__()
        self.__text_field.bind("<KeyRelease>", self.__on_key_released)
        # ˄

    # Set enable/disable from the Mediator
    def set_activation(self, is_enable):
        # ˅
        if is_enable:
            self.__text_field.configure(state = NORMAL)
        else:
            self.__text_field.configure(state = DISABLED)
        # ˄

    def is_empty(self):
        # ˅
        return self.__is_empty
        # ˄

    def __on_key_released(self, event):
        # ˅
        if len(self.__text_field.get()) == 0:
            self.__is_empty = True
        else:
            self.__is_empty = False

        self.mediator.colleague_changed()
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄