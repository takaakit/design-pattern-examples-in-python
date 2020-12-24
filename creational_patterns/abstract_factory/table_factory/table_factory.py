#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.factory import Factory
from creational_patterns.abstract_factory.table_factory.table_data import TableData
from creational_patterns.abstract_factory.table_factory.table_link import TableLink
from creational_patterns.abstract_factory.table_factory.table_page import TablePage

# ˄


class TableFactory(Factory):
    # ˅

    # ˄

    def create_page(self, title, author):
        # ˅
        return TablePage(title, author)
        # ˄

    def create_link(self, name, url):
        # ˅
        return TableLink(name, url)
        # ˄

    def create_data(self, name):
        # ˅
        return TableData(name)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
