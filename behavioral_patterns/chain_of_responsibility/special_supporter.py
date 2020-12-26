#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.chain_of_responsibility.supporter import Supporter

# ˄


class SpecialSupporter(Supporter):
    # ˅

    # ˄

    def __init__(self, name, target_id):

        self.__target_id = target_id

        # ˅
        Supporter.__init__(self, name)
        # ˄

    # Troubles with the specific ID are handled.
    def can_handle(self, trouble):
        # ˅
        return trouble.id == self.__target_id
        # ˄

    # ˅

    # ˄


# ˅

# ˄
