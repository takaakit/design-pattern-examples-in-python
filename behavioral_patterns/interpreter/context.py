#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


# Hold data which will be interpreted.
class Context(object):
    # ˅

    # ˄

    def __init__(self, line):

        self.__iter = iter(line.split())

        self.__current_token = None

        # ˅
        self.next_token()
        # ˄

    def next_token(self):
        # ˅
        try:
            self.__current_token = next(self.__iter)
        except StopIteration:
            self.__current_token = None
        return self.__current_token
        # ˄

    def get_token(self):
        # ˅
        return self.__current_token
        # ˄

    def slide_token(self, token):
        # ˅
        if token != self.__current_token:
            exit('WARNING: ' + token + ' is expected but ' + str(self.__current_token) + ' was found.')
        self.next_token()
        # ˄

    def get_number(self):
        # ˅
        if str(self.get_token()).isdigit():
            return self.get_token()
        else:
            exit('WARNING: ' + str(self.get_token()))
        # ˄

    # ˅

    # ˄


# ˅

# ˄
