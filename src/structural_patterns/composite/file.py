#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.composite.file_system_element import FileSystemElement

# ˄


class File(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name, size):
        # ˅
        super().__init__(name, size)
        # ˄

    # Print this element with the "upperPath".
    def print(self, upper_path):
        # ˅
        print(upper_path + '/' + self.to_string())
        # ˄

    # ˅

    # ˄


# ˅

# ˄
