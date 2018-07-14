#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creational_patterns.factory_method.id_card.credit_card_factory import CreditCardFactory

# Factory to make ID cards.

if __name__ == '__main__':
    factory = CreditCardFactory()

    jackson_card = factory.create('Jacson')
    jackson_card.use()

    sophia_card = factory.create('Sophia')
    sophia_card.use()

    olivia_card = factory.create('Olivia')
    olivia_card.use()
