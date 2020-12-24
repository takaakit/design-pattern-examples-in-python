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
        return self.create_product(owner)
        # ˄

    @abstractmethod
    def create_product(self, owner):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
