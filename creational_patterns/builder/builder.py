#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Builder(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def create_title(self, title):
        # ˅
        pass
        # ˄

    @abstractmethod
    def create_section(self, section):
        # ˅
        pass
        # ˄

    @abstractmethod
    def create_items(self, items):
        # ˅
        pass
        # ˄

    @abstractmethod
    def close(self):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
