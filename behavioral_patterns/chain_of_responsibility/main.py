#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.chain_of_responsibility.lazy_supporter import LazySupporter
from behavioral_patterns.chain_of_responsibility.moody_supporter import MoodySupporter
from behavioral_patterns.chain_of_responsibility.special_supporter import SpecialSupporter
from behavioral_patterns.chain_of_responsibility.limited_supporter import LimitedSupporter
from behavioral_patterns.chain_of_responsibility.trouble import Trouble

'''
A trouble is turned around among supporters, and the trouble will be handled by the supporter who can handle it. There are four types of supporters below:
* LazySupporter doesn't handle any trouble
* MoodySupporter handles odd ID troubles
* SpecialSupporter handles a trouble of the target ID.
* LimitedSupporter handles troubles below the limit ID.
'''

if __name__ == '__main__':
    emily = LazySupporter('Emily')
    william = MoodySupporter('William')
    amelia = SpecialSupporter('Amelia', 6)
    joseph = LimitedSupporter('Joseph', 5)

    # Make a chain.
    emily.set_next(william).set_next(amelia).set_next(joseph)

    # Various troubles occurred.
    for i in range(0, 10):
        emily.support(Trouble(i))
