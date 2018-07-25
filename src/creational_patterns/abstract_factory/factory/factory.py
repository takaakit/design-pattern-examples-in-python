#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *
from creational_patterns.abstract_factory.factory.data import Data
from creational_patterns.abstract_factory.factory.link import Link
from creational_patterns.abstract_factory.factory.page import Page

# ˄


class Factory(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def create_page(self, title, author):
        # ˅
        pass
        # ˄

    @abstractmethod
    def create_link(self, name, url):
        # ˅
        pass
        # ˄

    @abstractmethod
    def create_data(self, name):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅
from creational_patterns.abstract_factory.list_factory.list_factory import ListFactory
from creational_patterns.abstract_factory.table_factory.table_factory import TableFactory
def get_factory(class_name):
    cls = globals()[class_name]
    return cls()
# ˄
