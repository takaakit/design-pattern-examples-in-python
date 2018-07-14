#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.visitor.file_system_element import FileSystemElement

# ˄


class File(FileSystemElement):
    # ˅

    # ˄

    def __init__(self, name, size):
        # ˅
        super().__init__(name, size)
        # ˄

    def accept(self, visitor):
        # ˅
        visitor.visit_file(self)
        # ˄

    # ˅

    # ˄


# ˅

# ˄
