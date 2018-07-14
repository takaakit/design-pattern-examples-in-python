#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from time import sleep
from behavioral_patterns.observer.observer import Observer

# ˄


# Display values with a bar chart.
class BarChartObserver(Observer):
    # ˅

    # ˄

    def update(self, number):
        # ˅
        print('Bar chart: ', end="")
        for i in range(0, number.value):
            print('*', end="")
        print('')
        sleep(0.1)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
