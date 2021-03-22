#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.observer.subject import Subject

# ˄


# Generate a random number.
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
        self.__value = value
        self.notify_observers()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
