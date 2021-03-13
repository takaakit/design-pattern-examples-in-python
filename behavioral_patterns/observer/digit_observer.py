#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from time import sleep
from behavioral_patterns.observer.observer import Observer

# ˄


# Display values as a number.
class DigitObserver(Observer):
    # ˅

    # ˄

    def update(self, number):
        # ˅
        print('Digit    : ' + str(number.value))
        sleep(0.1)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
