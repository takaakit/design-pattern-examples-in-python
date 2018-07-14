#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.proxy.printer_proxy import PrinterProxy

# At the time of printing, create an instance of the printer for the first time.
# In order to spend time creating a printer, call a heavy task when creating a printer instance.

if __name__ == '__main__':
    p = PrinterProxy('Emily\'s printer')
    print('The current printer is ' + p.get_printer_name() + '.')
    p.set_printer_name('William\'s printer')
    print('The current printer is ' + p.get_printer_name() + '.')
    p.output('Nice to meet you.')
