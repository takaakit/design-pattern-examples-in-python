#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

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

# ˄
