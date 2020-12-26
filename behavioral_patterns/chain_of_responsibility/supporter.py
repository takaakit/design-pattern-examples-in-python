#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Supporter(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, name):

        # Supporter name
        self.__name = name

        # Next supporter
        self.__next = None

        # ˅
        pass
        # ˄

    # Trouble support
    # Troubles are sent around.
    def support(self, trouble):
        # ˅
        if self.can_handle(trouble):
            self.__supported(trouble)

        elif self.__next is not None:
            self.__next.support(trouble)

        else:
            self.__unsupported(trouble)
        # ˄

    # Set a next supporter.
    def set_next(self, next):
        # ˅
        self.__next = next
        return self.__next
        # ˄

    def to_string(self):
        # ˅
        return '[' + self.__name + ']'
        # ˄

    @abstractmethod
    def can_handle(self, trouble):
        # ˅
        pass
        # ˄

    # Trouble was supported.
    def __supported(self, trouble):
        # ˅
        print(trouble.to_string() + ' was handled by ' + self.__name + '.')
        # ˄

    # Trouble was unsupported.
    def __unsupported(self, trouble):
        # ˅
        print(trouble.to_string() + ' was not handled.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
