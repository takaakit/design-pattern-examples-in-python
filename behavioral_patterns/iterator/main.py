#!/usr/bin/env python
# -*- coding: utf-8 -*-
from behavioral_patterns.iterator.book import Book
from behavioral_patterns.iterator.book_shelf import BookShelf

'''
Add books in a bookshelf and display the names of the book in turn.
'''

if __name__ == '__main__':
    book_shelf = BookShelf(5)
    book_shelf.add(Book('Design Patterns: Elements of Reusable Object-Oriented Software'))
    book_shelf.add(Book('The Object Primer: Agile Model-Driven Development with UML 2.0'))
    book_shelf.add(Book('Software Systems Architecture: Working With Stakeholders Using Viewpoints and Perspectives'))
    book_shelf.add(Book('A Practical Guide to SysML: The Systems Modeling Language'))
    book_shelf.add(Book('A Pattern Language: Towns, Buildings, Construction'))

    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.title)
