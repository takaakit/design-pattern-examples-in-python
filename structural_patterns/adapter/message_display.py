#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class MessageDisplay(object):
    # ˅

    # ˄

    def __init__(self, message):

        self.__message = message

        # ˅
        pass
        # ˄

    def display_with_hyphens(self):
        # ˅
        print('-- ' + self.__message + ' --')
        # ˄

    def display_with_brackets(self):
        # ˅
        print('[[ ' + self.__message + ' ]]')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
