#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from creational_patterns.abstract_factory.factory.item import Item

# ˄


class Data(Item, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, name):

        self.items = []

        # ˅
        super().__init__(name)
        # ˄

    def add(self, item):
        # ˅
        self.items.append(item)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
