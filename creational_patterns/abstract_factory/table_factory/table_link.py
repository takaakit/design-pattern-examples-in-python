#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.link import Link

# ˄


class TableLink(Link):
    # ˅

    # ˄

    def __init__(self, name, url):
        # ˅
        super().__init__(name, url)
        # ˄

    def to_html(self):
        # ˅
        return f'  <td><a href="{self.url}">{self.name}</a></td>\n'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
