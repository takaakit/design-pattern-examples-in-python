#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.composite.file_system_element import FileSystemElement

# ˄


class File(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name, size):

        self.__name = name

        self.__size = size

        # ˅
        super().__init__()
        # ˄

    def get_name(self):
        # ˅
        return self.__name
        # ˄

    def get_size(self):
        # ˅
        return self.__size
        # ˄

    # Print this element with the "upper_path".
    def print(self, upper_path):
        # ˅
        print(f'{upper_path}/{self.to_string()}')
        # ˄

    # ˅

    # ˄


# ˅

# ˄
