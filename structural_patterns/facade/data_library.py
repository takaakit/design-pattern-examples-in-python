#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import configparser

# ˄


class DataLibrary(object):
    # ˅
    
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
