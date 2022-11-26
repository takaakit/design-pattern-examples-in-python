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
        # Before processing, it checks to make sure the changed subject is the subject held.
        if changedSubject is self.__numberSubject:
            print('Bar chart: ' + ('*' * self.__numberSubject.value))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
