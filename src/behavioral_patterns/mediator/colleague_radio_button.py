#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from tkinter import *
from behavioral_patterns.mediator.colleague import Colleague

# ˄


class ColleagueRadioButton(Colleague):
    # ˅

    # ˄

    # Numerical value of the selected radio button
    __selected_value = 0

    def __init__(self, radio_button):

        self.__radio_button = radio_button

        # ˅
        self.__radio_button.bind('<ButtonRelease-1>', self.__on_mouse_released)
        # ˄

    # Set enable/disable from the Mediator
    def set_activation(self, is_enable):
        # ˅
        if is_enable:
            self.__radio_button.configure(state = NORMAL)
        else:
            self.__radio_button.configure(state = DISABLED)
        # ˄

    def is_selected(self):
        # ˅
        return ColleagueRadioButton.__selected_value == self.__radio_button['value']
        # ˄

    def __on_mouse_released(self, event):
        # ˅
        ColleagueRadioButton.__selected_value = int(event.widget['value'])
        self.mediator.colleague_changed()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
