#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from behavioral_patterns.visitor.element import Element

# ˄


class FileSystemElement(Element, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def get_name(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_size(self):
        # ˅
        pass
        # ˄

    def to_string(self):
        # ˅
        return self.get_name() + ' (' + str(self.get_size()) + ')'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
