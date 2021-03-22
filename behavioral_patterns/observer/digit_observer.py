#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.observer.observer import Observer

# ˄


# Display values as a number.
class DigitObserver(Observer):
    # ˅

    # ˄

    def __init__(self, numberSubject):

        self.__numberSubject = numberSubject

        # ˅
        pass
        # ˄

    def update(self, changedSubject):
        # ˅
        if changedSubject is self.__numberSubject:
            print('Digit    : ' + str(self.__numberSubject.value))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
