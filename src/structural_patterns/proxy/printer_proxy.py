#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.proxy.printer import Printer
from structural_patterns.proxy.real_printer import RealPrinter

# ˄


class PrinterProxy(Printer):
    # ˅

    # ˄

    def __init__(self, name):

        self.__current_name = name

        self.printer_name = None

        # A printer that actually prints
        self.__real = None

        # ˅
        pass
        # ˄

    def get_printer_name(self):
        # ˅
        return self.__current_name
        # ˄

    def set_printer_name(self, value):
        # ˅
        if self.__real is not None:
            self.__real.printer_name = value
            self.__current_name = value
        # ˄

    def output(self, content):
        # ˅
        self.__create_printer()
        if self.__real is not None:
            self.__real.output(content)
        # ˄

    # Create an actual printer
    def __create_printer(self):
        # ˅
        if self.__real is None:
            self.__real = RealPrinter(self.__current_name)
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
