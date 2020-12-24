#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Colleague(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def __init__(self):

        self.mediator = None

        # ˅
        pass
        # ˄

    def set_mediator(self, mediator):
        # ˅
        self.mediator = mediator
        # ˄

    # Set enable/disable from the Mediator
    @abstractmethod
    def set_activation(self, is_enable):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
