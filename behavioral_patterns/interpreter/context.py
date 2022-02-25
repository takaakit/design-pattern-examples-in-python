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

        self.__current_iter = self.__iter

        self.__iter_number = 0

        self.__text_size = len(line.split())

        # ˅
        self.next_token()
        # ˄

    def next_token(self):
        # ˅
        if self.__iter_number < self.__text_size:
            self.__current_iter = next(self.__iter)
            self.__iter_number += 1
        else:
            self.__current_iter = None
        return self.__current_iter
        # ˄

    def get_token(self):
        # ˅
        return self.__current_iter
        # ˄

    def slide_token(self, token):
        # ˅
        if token != self.__current_iter:
            exit('WARNING: ' + token + ' is expected but ' + str(self.__current_iter) + ' was found.')
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
