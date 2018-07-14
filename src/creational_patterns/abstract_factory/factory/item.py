#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Item(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    def __init__(self, name):

        self.name = name

        # ˅
        pass
        # ˄

    @abstractmethod
    def to_html(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
