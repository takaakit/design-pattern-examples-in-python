#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.factory_method.framework.factory import Factory
from creational_patterns.factory_method.id_card.credit_card import CreditCard

# ˄


class CreditCardFactory(Factory):
    # ˅

    # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    def create_product(self, owner):
        # ˅
        return CreditCard(owner)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
