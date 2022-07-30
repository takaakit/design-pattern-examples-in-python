#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.proxy.printer import Printer
from structural_patterns.proxy.real_printer import RealPrinter

# ˄


# ProxyPrinter forwards requests to RealPrinter when appropriate.
class ProxyPrinter(Printer):
    # ˅

    # ˄

    def __init__(self, name):

        self.__current_name = name

        # A printer that actually prints
        self.__real = None

        # ˅
        pass
        # ˄

    def get_name(self):
        # ˅
        if self.__real is not None:
            return self.__real.get_name()
        else:
            return self.__current_name
        # ˄

    def change_name(self, name):
        # ˅
        if self.__real is not None:
            self.__real.change_name(name)

        self.__current_name = name
        # ˄

    def output(self, content):
        # ˅
        # Check to see if the the RealPrinter had been created, create it if necessary.
        if self.__real is None:
            self.__real = RealPrinter(self.__current_name)

        self.__real.output(content)
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
