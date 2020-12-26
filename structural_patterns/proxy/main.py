#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.proxy.printer_proxy import PrinterProxy

'''
Print on a named printer. Setting and changing the printer name is done by Proxy("PrinterProxy"). At the time of printing, create an instance of the RealSubject("RealPrinter") for the first time.
'''

if __name__ == '__main__':
    p = PrinterProxy('PRINTER-A')
    print('The printer name is ' + p.get_printer_name() + '.')
    p.set_printer_name('PRINTER-B')
    print('The printer name is ' + p.get_printer_name() + '.')

    print('Print start.')
    p.output('Nice to meet you.')
    print('Print exit.')
