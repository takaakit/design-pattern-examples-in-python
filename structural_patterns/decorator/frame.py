#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from structural_patterns.decorator.display import Display

# ˄


class Frame(Display, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, display):

        self.display = display

        # ˅
        super().__init__()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
