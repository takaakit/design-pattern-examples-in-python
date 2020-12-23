#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class Directory(object):
    # ˅

    # ˄

    def __init__(self, builder):

        self.__builder = builder

        # ˅
        pass
        # ˄

    # Construct a document
    def build(self):
        # ˅
        self.__builder.create_title('Greeting')                                      # Title
        self.__builder.create_section('Morning and Afternoon')                       # Section
        self.__builder.create_items(['Good morning.', 'Hello.'])                     # Items
        self.__builder.create_section('Evening')                                     # Other section
        self.__builder.create_items(['Good evening.', 'Good night.', 'Goodbye.'])    # Other items
        self.__builder.close()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
