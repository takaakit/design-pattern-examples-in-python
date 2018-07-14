#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.composite.file_system_element import FileSystemElement

# ˄


class Directory(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name):

        self.__elements = []

        # ˅
        super().__init__(name, 0)
        # ˄

    # Print this element with the "upperPath".
    def print(self, upper_path):
        # ˅
        print(upper_path + '/' + self.to_string())
        for element in self.__elements:
            element.print(upper_path + '/' + self.name)
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
