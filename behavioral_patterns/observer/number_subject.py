#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.observer.subject import Subject

# ˄


# Holds a value and notifies observers when the value is set.
class NumberSubject(Subject):
    # ˅

    # ˄

    def __init__(self):

        self.__value = 0

        # ˅
        super().__init__()
        # ˄

    @property
    def value(self):
        # ˅
        return self.__value
        # ˄

    @value.setter
    def value(self, value):
        # ˅
        # Notify observers when the value is set.
        self.__value = value
        self.notify_observers()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
