#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.chain_of_responsibility.supporter import Supporter

# ˄


class MoodySupporter(Supporter):
    # ˅

    # ˄

    def __init__(self, name):
        # ˅
        Supporter.__init__(self, name)
        # ˄

    # Troubles with an odd ID are handled.
    def handle(self, trouble):
        # ˅
        return trouble.id % 2 == 1
        # ˄

    # ˅

    # ˄


# ˅

# ˄
