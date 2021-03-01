#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import configparser

# ˄


class DataLibrary(object):
    # ˅
    
    # ˄

    __instance = None

    @classmethod
    def get_instance(cls):
        # ˅
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
        # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    # Read a data library file.
    def get_properties(self, data_library_name):
        # ˅
        prop = configparser.ConfigParser()
        prop.read(data_library_name, 'UTF-8')

        return prop
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
