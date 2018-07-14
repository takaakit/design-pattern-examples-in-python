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

        self.__card_owners = []

        # ˅
        pass
        # ˄

    def create_product(self, owner):
        # ˅
        return CreditCard(owner)
        # ˄

    def register_product(self, product):
        # ˅
        self.__card_owners.append(product)
        # ˄

    def get_card_owner(self):
        # ˅
        return self.__card_owners
        # ˄

    # ˅

    # ˄


# ˅

# ˄
