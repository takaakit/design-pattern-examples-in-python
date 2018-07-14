#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from time import sleep
from behavioral_patterns.observer.observer import Observer

# ˄


# Display values with digits.
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
