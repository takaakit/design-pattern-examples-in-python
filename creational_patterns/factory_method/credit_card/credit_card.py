#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.factory_method.framework.product import Product

# ˄


class CreditCard(Product):
    # ˅

    # ˄

    def __init__(self, owner):

        self.__owner = owner

        # ˅
        print(f'Make {self.__owner}\'s card.')
        # ˄

    def use(self):
        # ˅
        print(f'Use {self.__owner}\'s card.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
