#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.chain_of_responsibility.supporter import Supporter

# ˄


class LimitedSupporter(Supporter):
    # ˅

    # ˄

    def __init__(self, name, limit_id):

        self.__limit_id = limit_id

        # ˅
        Supporter.__init__(self, name)
        # ˄

    # Troubles with an ID below the limit are handled.
    def can_handle(self, trouble):
        # ˅
        return trouble.id <= self.__limit_id
        # ˄

    # ˅

    # ˄


# ˅

# ˄
