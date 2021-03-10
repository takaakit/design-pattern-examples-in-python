#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.factory_method.credit_card.credit_card_factory import CreditCardFactory

'''
The subject is a factory to make credit cards. The Factory defines how to create an credit card,
but the actual credit card is created by the CreditCardFactory.
The "createProduct()" is called a Factory Method, and it is responsible for manufacturing an object.
'''

if __name__ == '__main__':
    factory = CreditCardFactory()

    jackson_card = factory.create('Jacson')
    jackson_card.use()

    sophia_card = factory.create('Sophia')
    sophia_card.use()

    olivia_card = factory.create('Olivia')
    olivia_card.use()
