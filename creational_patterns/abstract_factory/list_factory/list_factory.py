#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.factory import Factory
from creational_patterns.abstract_factory.list_factory.list_data import ListData
from creational_patterns.abstract_factory.list_factory.list_link import ListLink
from creational_patterns.abstract_factory.list_factory.list_page import ListPage

# ˄


class ListFactory(Factory):
    # ˅

    # ˄

    def create_page(self, title, author):
        # ˅
        return ListPage(title, author)
        # ˄

    def create_link(self, name, url):
        # ˅
        return ListLink(name, url)
        # ˄

    def create_data(self, name):
        # ˅
        return ListData(name)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
