#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Visitor(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def visit_file(self, file):
        # ˅
        pass
        # ˄

    @abstractmethod
    def visit_directory(self, directory):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
