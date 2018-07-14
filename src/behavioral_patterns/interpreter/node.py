#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


# Node in the syntax tree.
class Node(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def parse(self, context):
        # ˅
        pass
        # ˄

    @abstractmethod
    def to_string(self):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
