#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class PaintingTarget(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def paint(self, x, y):
        # ˅
        pass
        # ˄

    @abstractmethod
    def clear(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
