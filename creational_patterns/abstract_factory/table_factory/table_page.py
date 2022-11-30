#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.abstract_factory.factory.page import Page

# ˄


class TablePage(Page):
    # ˅
    
    # ˄

    def __init__(self, title, author):
        # ˅
        super().__init__(title, author)
        # ˄

    def to_html(self):
        # ˅
        buffer = list()
        buffer.append(f'<html><head><title>{self.title}</title></head><body>\n')
        buffer.append(f'<h1>{self.title}</h1>\n')
        buffer.append('<table width="80%" border="3">\n')
        for content in self.contents:
            buffer.append(f'<tr>{content.to_html()}</tr>\n')
        buffer.append('</table>\n')
        buffer.append(f'<hr><address>{self.author}</address>\n')
        buffer.append('</body></html>\n')
        return ''.join(buffer)
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
