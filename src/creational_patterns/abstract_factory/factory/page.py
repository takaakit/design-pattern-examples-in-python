#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from creational_patterns.abstract_factory.factory.item import Item

# ˄


class Page(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self, title, author):

        self.title = title

        self.author = author

        self.contents = []

        # ˅
        pass
        # ˄

    @abstractmethod
    def to_html(self):
        # ˅
        pass
        # ˄

    def add(self, item):
        # ˅
        self.contents.append(item)
        # ˄

    def output(self):
        # ˅
        file_name = self.title + '.html'
        file = open(file_name, 'w')
        file.write(self.to_html())
        file.close()
        print(file_name + ' has been created.')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
