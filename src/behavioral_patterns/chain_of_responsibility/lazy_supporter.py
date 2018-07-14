#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.chain_of_responsibility.supporter import Supporter
# ˄


class LazySupporter(Supporter):
    # ˅

    # ˄

    def __init__(self, name):
        # ˅
        Supporter.__init__(self, name)
        # ˄

    # No troubles are handled.
    def handle(self, trouble):
        # ˅
        return False
        # ˄

    # ˅

    # ˄


# ˅

# ˄
