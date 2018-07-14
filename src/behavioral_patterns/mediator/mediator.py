#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Mediator(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def colleague_changed(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def create_colleagues(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
