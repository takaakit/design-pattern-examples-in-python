#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.link import Link

# ˄


class ListLink(Link):
    # ˅

    # ˄

    def __init__(self, name, url):
        # ˅
        super().__init__(name, url)
        # ˄

    def to_html(self):
        # ˅
        return '  <li><a href=\"' + self.url + '\">' + self.name + '</a></li>\n'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
