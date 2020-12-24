#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Element(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def accept(self, visitor):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
