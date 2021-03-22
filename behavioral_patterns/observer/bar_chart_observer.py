#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.observer.observer import Observer

# ˄


# Display values as a bar chart.
class BarChartObserver(Observer):
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
            print('Bar chart: ', end="")
            for i in range(0, self.__numberSubject.value):
                print('*', end="")
            print('')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
