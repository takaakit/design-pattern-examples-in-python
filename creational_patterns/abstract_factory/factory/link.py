#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from creational_patterns.abstract_factory.factory.item import Item

# ˄


class Link(Item, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, name, url):

        self.url = url

        # ˅
        super().__init__(name)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
