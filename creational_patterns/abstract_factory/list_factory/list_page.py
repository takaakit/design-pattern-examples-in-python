#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.page import Page

# ˄


class ListPage(Page):
    # ˅

    # ˄

    def __init__(self, title, author):
        # ˅
        super().__init__(title, author)
        # ˄

    def to_html(self):
        # ˅
        buffer = list()
        buffer.append('<html><head><title>' + self.title + '</title></head>\n')
        buffer.append('<body><h1>' + self.title + '</h1>\n')
        buffer.append('<ul>\n')
        for content in self.contents:
            buffer.append(content.to_html())
        buffer.append('</ul>\n')
        buffer.append('<hr><address>' + self.author + '</address>')
        buffer.append('</body></html>\n')
        return ''.join(buffer)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
