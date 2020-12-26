#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.iterator.iterator import Iterator

# ˄


class BookShelfIterator(Iterator):
    # ˅

    # ˄

    def __init__(self, book_shelf):

        self.__index = 0

        self.__book_shelf = book_shelf

        # ˅
        pass
        # ˄

    def has_next(self):
        # ˅
        return self.__index < self.__book_shelf.get_number_of_books()
        # ˄

    def next(self):
        # ˅
        book = self.__book_shelf.get_at(self.__index)
        self.__index += 1
        return book
        # ˄

    # ˅

    # ˄


# ˅

# ˄
