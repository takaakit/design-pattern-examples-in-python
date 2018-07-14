#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.iterator.aggregate import Aggregate

# ˄


class BookShelf(Aggregate):
    # ˅

    # ˄

    def __init__(self, max_size):

        self.number_of_books = 0

        self.__books = [None] * max_size

        # ˅
        pass
        # ˄

    def iterator(self):
        # ˅
        from behavioral_patterns.iterator.book_shelf_iterator import BookShelfIterator
        return BookShelfIterator(self)
        # ˄

    def get_at(self, index):
        # ˅
        return self.__books[index]
        # ˄

    def add(self, book):
        # ˅
        self.__books[self.number_of_books] = book
        self.number_of_books += 1
        # ˄

    # ˅

    # ˄


# ˅

# ˄
