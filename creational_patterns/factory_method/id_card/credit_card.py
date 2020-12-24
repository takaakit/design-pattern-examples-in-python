#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.factory_method.framework.product import Product

# ˄


class CreditCard(Product):
    # ˅

    # ˄

    def __init__(self, owner):

        self.owner = owner

        # ˅
        print('Make ' + self.owner + '\'s card.')
        # ˄

    def use(self):
        # ˅
        print('User ' + self.owner + '\'s card.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
