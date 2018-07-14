#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Iterator(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def has_next(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def next(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
