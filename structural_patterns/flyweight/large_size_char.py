#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import os

# ˄


class LargeSizeChar(object):
    # ˅

    # ˄

    def __init__(self, char_name):

        self.__char_name = char_name

        # Display data of the large size character
        self.__display_data = ''

        # ˅
        try:
            reader = open(os.path.join(os.path.dirname(__file__), 'big' + char_name + '.txt'), 'r')
            buffer = []
            for line in reader:
                buffer.append(line)
            reader.close()
            self.__display_data = ''.join(buffer)
        except IOError:
            self.__display_data = char_name + '?'
        # ˄

    # Display the large size character
    def display(self):
        # ˅
        print(self.__display_data)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
