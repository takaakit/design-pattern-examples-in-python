#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Printer(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def get_name(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def change_name(self, name):
        # ˅
        pass
        # ˄

    @abstractmethod
    def output(self, content):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
