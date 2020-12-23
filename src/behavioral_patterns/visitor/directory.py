#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.visitor.file_system_element import FileSystemElement

# ˄


class Directory(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name):

        self.__name = name

        # Collection of elements
        self.__elements = []

        # ˅

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

    # Directory name
    def get_name(self):
        # ˅
        return self.__name
        # ˄

    # Directory size
    def get_size(self):
        # ˅
        size = 0
        for element in self.__elements:
            size += element.get_size()
        return size
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
