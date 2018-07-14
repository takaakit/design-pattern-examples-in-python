#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from behavioral_patterns.visitor.element import Element

# ˄


class FileSystemElement(Element, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, name, size):

        self.name = name

        self.size = size

        # ˅
        pass
        # ˄

    def to_string(self):
        # ˅
        return self.name + ' (' + str(self.size) + ')'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
