#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.observer.number import Number

# ˄


# Generate a random number.
class RandomNumber(Number):
    # ˅

    # ˄

    def __init__(self):
        # ˅
        super(RandomNumber, self).__init__()
        # ˄

    def generate(self):
        # ˅
        for i in range(0, 20, 1):
            self.value = random.randrange(50)
            self.notify_observers()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
