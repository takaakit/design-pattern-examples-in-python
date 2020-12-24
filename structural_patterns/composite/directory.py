#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.composite.file_system_element import FileSystemElement

# ˄


class Directory(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name):

        self.__name = name

        self.__elements = []

        # ˅
        super().__init__()
        # ˄

    def get_name(self):
        # ˅
        return self.__name
        # ˄

    def get_size(self):
        # ˅
        size = 0
        for element in self.__elements:
            size += element.get_size()
        return size
        # ˄

    # Print this element with the "upper_path".
    def print(self, upper_path):
        # ˅
        print(upper_path + '/' + self.to_string())
        for element in self.__elements:
            element.print(upper_path + '/' + self.get_name())
        # ˄

    # Add a element
    def add(self, element):
        # ˅
        self.__elements.append(element)
        return self
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
