#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Display(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def create_clone(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def show(self, message):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
