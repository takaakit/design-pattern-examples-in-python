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
        # Write pre-creation code here.

        # Encapsulate the knowledge of which Product subclass to create and move this knowledge out of the framework.
        product = self.create_product(owner)

        # Write post-creation code here.

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
