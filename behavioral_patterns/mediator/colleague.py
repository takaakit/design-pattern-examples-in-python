#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Colleague(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def __init__(self):

        self.__mediator = None

        # ˅
        pass
        # ˄

    # Set enable/disable from the Mediator
    @abstractmethod
    def set_activation(self, is_enable):
        # ˅
        pass
        # ˄

    @property
    def mediator(self):
        # ˅
        return self.__mediator
        # ˄

    @mediator.setter
    def mediator(self, value):
        # ˅
        self.__mediator = value
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
