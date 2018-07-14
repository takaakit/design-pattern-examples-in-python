#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.flyweight.large_size_char import LargeSizeChar

# ˄


class LargeSizeCharFactory(object):
    # ˅

    # ˄

    __instance = None

    def __init__(self):

        self.__pool_chars = {}

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

    # Create an instance of the large size character.
    def get_large_size_char(self, char_name):
        # ˅
        lsc = self.__pool_chars.get(char_name)
        if lsc is None:
            lsc = LargeSizeChar(char_name)       # Create an instance
            self.__pool_chars[char_name] = lsc
        return lsc
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
