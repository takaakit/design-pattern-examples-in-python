#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.visitor.file_system_element import FileSystemElement

# ˄


class Directory(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name):

        # Collection of elements
        self.__elements = []

        # ˅
        super().__init__(name, 0)
        # ˄

    # Accept a visitor
    def accept(self, visitor):
        # ˅
        visitor.visit_directory(self)
        # ˄

    # Add an entry
    def add(self, element):
        # ˅
        self.__elements.append(element)
        return self
        # ˄

    # Create a iterator
    def __iter__(self):
        # ˅
        return iter(self.__elements)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
