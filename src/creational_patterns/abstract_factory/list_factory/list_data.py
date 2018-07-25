#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.data import Data

# ˄


class ListData(Data):
    # ˅

    # ˄

    def __init__(self, name):
        # ˅
        super().__init__(name)
        # ˄

    def to_html(self):
        # ˅
        buffer = []
        buffer.append('<li>' + self.name + '<ul>\n')
        for item in self.items:
            buffer.append(item.to_html())
        buffer.append('</ul></li>\n')
        return ''.join(buffer)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
