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
            exit(f'ERROR: {token} is expected but {self.__current_token} was found.')
        self.next_token()
        # ˄

    def get_number(self):
        # ˅
        if str(self.__current_token).isdigit():
            return self.__current_token
        else:
            exit(f'ERROR: {self.__current_token} is not degit.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
