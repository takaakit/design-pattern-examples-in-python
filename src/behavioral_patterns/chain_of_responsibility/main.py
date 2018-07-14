#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.chain_of_responsibility.lazy_supporter import LazySupporter
from behavioral_patterns.chain_of_responsibility.moody_supporter import MoodySupporter
from behavioral_patterns.chain_of_responsibility.special_supporter import SpecialSupporter
from behavioral_patterns.chain_of_responsibility.limited_supporter import LimitedSupporter
from behavioral_patterns.chain_of_responsibility.trouble import Trouble

# Someone handles a trouble.

if __name__ == '__main__':
    emily = LazySupporter('Emily')
    william = MoodySupporter('William')
    amelia = SpecialSupporter('Amelia', 153)
    michael = LimitedSupporter('Michael', 340)
    joseph = LimitedSupporter('Joseph', 250)
    lily = LimitedSupporter('Lily', 350)

    # Make a chain.
    emily.set_next(william).set_next(amelia).set_next(michael).set_next(joseph).set_next(lily)

    # Various troubles occurred.
    for i in range(0, 500, 17):
        emily.support(Trouble(i))
