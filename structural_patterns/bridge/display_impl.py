#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class DisplayImpl(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def impl_open(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def impl_write(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def impl_close(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
