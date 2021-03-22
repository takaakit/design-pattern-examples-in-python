#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


# An abstract class that generates numbers.
class Subject(object):
    # ˅

    # ˄

    def __init__(self):

        self.__observers = []

        # ˅
        pass
        # ˄

    def attach(self, observer):
        # ˅
        self.__observers.append(observer)
        # ˄

    def detach(self, observer):
        # ˅
        self.__observers.remove(observer)
        # ˄

    def notify_observers(self):
        # ˅
        for observer in self.__observers:
            observer.update(self)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
