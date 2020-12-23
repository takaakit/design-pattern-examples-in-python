#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Factory(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def create(self, owner):
        # ˅
        product = self.create_product(owner)
        self.register_product(product)
        return product
        # ˄

    @abstractmethod
    def create_product(self, owner):
        # ˅
        pass
        # ˄

    @abstractmethod
    def register_product(self, product):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
