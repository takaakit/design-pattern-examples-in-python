#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class Singleton(object):
    # ˅

    # ˄

    __instance = None

    def __init__(self):
        # ˅
        pass
        # ˄

    @classmethod
    def get_instance(cls):
        # ˅
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
        # ˄

    # ˅

    # ˄


# ˅

# ˄
