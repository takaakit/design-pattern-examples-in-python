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
        file_name = data_library_name + '.txt'
        prop = configparser.ConfigParser()
        prop.read(file_name, 'UTF-8')

        return prop
        # ˄

    # ˅

    # ˄


# ˅

# ˄
