#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from creational_patterns.abstract_factory.list_factory.list_factory import ListFactory
from creational_patterns.abstract_factory.table_factory.table_factory import TableFactory

'''
Create a hierarchical link collection as an HTML file. It can be created in either tabular or list format.
'''

if __name__ == '__main__':
    print('Please enter a number (1 or 2):')
    print('  1: Create objects by using ListFactory')
    print('  2: Create objects by using TableFactory')
    input_value = input()
    number = 0
    try:
        number = int(input_value)
    except ValueError:
        print('Unexpected value.')
        sys.exit(1)

    factory = None
    if number == 1:
        factory = ListFactory()
    elif number == 2:
        factory = TableFactory()
    else:
        print('The value is not 1 or 2.')
        sys.exit(1)

    washington_post = factory.create_link('The Washington Post', 'https://www.washingtonpost.com/')
    new_york_times = factory.create_link('The NewYork Times', 'https://www.nytimes.com/')
    financial_times = factory.create_link('The Financial Times', 'https://www.ft.com/')

    newspaper = factory.create_data('Newspaper')
    newspaper.add(washington_post)
    newspaper.add(new_york_times)
    newspaper.add(financial_times)

    yahoo = factory.create_link('Yahoo!', 'https://www.yahoo.com/')
    google = factory.create_link('Google', 'https://www.google.com/')

    search_engine = factory.create_data('Search engine')
    search_engine.add(yahoo)
    search_engine.add(google)

    link_page = factory.create_page('LinkPage', 'James Smith')
    link_page.add(newspaper)
    link_page.add(search_engine)

    link_page.output()
