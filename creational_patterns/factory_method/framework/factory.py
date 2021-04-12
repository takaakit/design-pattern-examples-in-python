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
        # Write pre-creation code here, if any.

        product = self.create_product(owner)

        # Write post-creation code here, if any.

        return product
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
