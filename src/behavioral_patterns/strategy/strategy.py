#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Strategy(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def next_hand(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def learn(self, win):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
