#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.visitor.file_system_element import FileSystemElement

# ˄


class File(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name, size):

        self.__name = name

        self.__size = size

        # ˅
        pass
        # ˄

    def accept(self, visitor):
        # ˅
        visitor.visit_file(file=self)
        # ˄

    # File name
    def get_name(self):
        # ˅
        return self.__name
        # ˄

    # File size
    def get_size(self):
        # ˅
        return self.__size
        # ˄

    # ˅

    # ˄


# ˅

# ˄
