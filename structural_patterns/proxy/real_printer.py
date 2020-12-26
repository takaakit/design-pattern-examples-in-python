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

        self.printer_name = name

        # ˅
        self.__heavy_task('Creating an instance(' + self.printer_name + ') of the Printer')
        # ˄

    # Display a content with the name
    def output(self, content):
        # ˅
        print('==========')
        print(content)
        print('Printed by ' + self.printer_name)
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