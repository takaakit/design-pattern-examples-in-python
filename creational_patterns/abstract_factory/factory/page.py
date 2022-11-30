#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import os
from abc import *

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
        file_name = f'{self.title}.html'
        with open(file_name, 'w') as f:
            f.write(self.to_html())
        print(f'{file_name} has been created.')
        print(f'Output File: {os.path.join(os.getcwd(), file_name)}')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
