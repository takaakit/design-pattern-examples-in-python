#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from creational_patterns.abstract_factory.factory.factory import get_factory

# Create a hierarchical link collection as an HTML file.

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('Usage: python main.py class.name.of.ConcreteFactory')
        print('Ex.1 : python main.py ListFactory')
        print('Ex.2 : python main.py TableFactory')
    else:
        factory = get_factory(args[1])

        washington_post = factory.create_link('The Washington Post', 'https://www.washingtonpost.com/')
        new_york_times = factory.create_link('The NewYork Times', 'https://www.nytimes.com/')
        financial_times = factory.create_link('The Financial Times', 'https://www.ft.com/')
        yahoo = factory.create_link('Yahoo!', 'https://www.yahoo.com/')
        google = factory.create_link('Google', 'https://www.google.com/')
        mlb = factory.create_link('MLB', 'https://www.mlb.com/')
        fifa = factory.create_link('FIFA', 'https://www.fifa.com/')
        wba = factory.create_link('WBA', 'http://www.wbaboxing.com/')
        wbc = factory.create_link('WBC', 'http://www.wbcboxing.com/')

        newspaper = factory.create_data('Newspaper')
        newspaper.add(washington_post)
        newspaper.add(new_york_times)
        newspaper.add(financial_times)

        search_engine = factory.create_data('Search engine')
        search_engine.add(yahoo)
        search_engine.add(google)

        sports = factory.create_data('Sports')
        sports.add(mlb)
        sports.add(fifa)
        sports.add(wba)
        sports.add(wbc)

        link_page = factory.create_page('LinkPage', 'James Smith')
        link_page.add(newspaper)
        link_page.add(search_engine)
        link_page.add(sports)

        link_page.output()
