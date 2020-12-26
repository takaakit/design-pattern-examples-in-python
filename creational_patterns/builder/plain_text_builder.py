#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.builder.builder import Builder

# ˄


class PlainTextBuilder(Builder):
    # ˅

    # ˄

    def __init__(self):

        # String to output
        self.__content = ''

        self.__buffer = []

        # ˅
        pass
        # ˄

    # Make a title of plain text
    def create_title(self, title):
        # ˅
        self.__buffer.append('--------------------------------\n')  # Decoration line
        self.__buffer.append('[' + title + ']\n')                   # Title
        self.__buffer.append('\n')                                  # Blank line
        # ˄

    # Make a section of plain text
    def create_section(self, section):
        # ˅
        self.__buffer.append('* ' + section + '\n')                 # Section
        self.__buffer.append('\n')                                  # Blank line
        # ˄

    # Make items of plain text
    def create_items(self, items):
        # ˅
        for item in items:
            self.__buffer.append('  - ' + item + '\n')              # Items
        self.__buffer.append('\n')                                  # Blank line
        # ˄

    def close(self):
        # ˅
        self.__buffer.append('--------------------------------\n')  # Decoration line
        self.__content = ''.join(self.__buffer)
        # ˄

    def get_content(self):
        # ˅
        return self.__content
        # ˄

    # ˅

    # ˄


# ˅

# ˄
