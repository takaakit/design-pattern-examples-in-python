#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from behavioral_patterns.observer.observer import Observer

# ˄


# An abstract class that generates numbers.
class Number(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self):

        self.value = 0

        self.__observers = []

        # ˅
        pass
        # ˄

    @abstractmethod
    def generate(self):
        # ˅
        pass
        # ˄

    def add_observer(self, observer):
        # ˅
        self.__observers.append(observer)
        # ˄

    def delete_observer(self, observer):
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
