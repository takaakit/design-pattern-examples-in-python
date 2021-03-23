#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from time import sleep
from structural_patterns.proxy.printer import Printer

# ˄


class RealPrinter(Printer):
    # ˅

    # ˄

    def __init__(self, name):

        self.__name = name

        # ˅
        self.__heavy_task('Creating an instance (' + self.__name + ') of the Printer')
        # ˄

    def get_name(self):
        # ˅
        return self.__name
        # ˄

    def change_name(self, name):
        # ˅
        self.__name = name
        # ˄

    # Display a content with the name
    def output(self, content):
        # ˅
        print('==========')
        print(content)
        print('Printed by ' + self.__name)
        print('==========')
        # ˄

    # Heavy task (Please think so...)
    def __heavy_task(self, message):
        # ˅
        print(message, end = '')
        for i in range(10):
            sleep(0.5)
            print('.', end = '')
        print('Done.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
