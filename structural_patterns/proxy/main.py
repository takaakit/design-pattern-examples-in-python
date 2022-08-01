#!/usr/bin/env python
# -*- coding: utf-8 -*-
from structural_patterns.proxy.printer import Printer
from structural_patterns.proxy.proxy_printer import ProxyPrinter

'''
Print on a named printer. Setting and changing the printer name is done by Proxy (ProxyPrinter).
At the time of printing, create an instance of the RealSubject (RealPrinter) for the first time.
'''

if __name__ == '__main__':
    p: Printer = ProxyPrinter(name='PRINTER-A')
    print('The printer name is ' + p.get_name() + '.')
    p.change_name(name='PRINTER-B')
    print('The printer name is ' + p.get_name() + '.')

    print('Print start.')
    p.output(content='Nice to meet you.')
    print('Print exit.')
