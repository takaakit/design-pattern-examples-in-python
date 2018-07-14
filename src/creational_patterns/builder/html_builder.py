#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from creational_patterns.builder.builder import Builder

# ˄


class HTMLBuilder(Builder):
    # ˅

    # ˄

    def __init__(self):

        # File name to create
        self.result = None

        self.__writer = None

        # ˅
        pass
        # ˄

    # Make a title of HTML file
    def create_title(self, title):
        # ˅
        self.result = title + '.html'       # Set a title as a file name
        self.__writer = open(self.result, 'w')
        self.__writer.write('<html><head><title>' + title + '</title></head><body>')
        self.__writer.write('<h1>' + title + '</h1>')
        # ˄

    # Make a section of HTML file
    def create_section(self, section):
        # ˅
        self.__writer.write('<p>' + section + '</p>')   # Write a section
        # ˄

    # Make items of HTML file
    def create_items(self, items):
        # ˅
        self.__writer.write('<ul>')         # Write items
        for item in items:
            self.__writer.write('<li>' + item + '</li>')
        self.__writer.write('</ul>')
        # ˄

    def close(self):
        # ˅
        self.__writer.write('</body></html>')
        self.__writer.close()               # Close file
        # ˄

    # ˅

    # ˄


# ˅

# ˄
