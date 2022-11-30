#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class FileSystemElement(object, metaclass=ABCMeta):
    # ˅

    # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_name(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def get_size(self):
        # ˅
        pass
        # ˄

    # Print this element with the "upper_path".
    @abstractmethod
    def print(self, upper_path):
        # ˅
        pass
        # ˄

    def to_string(self):
        # ˅
        return f'{self.get_name()} ({self.get_size()})'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
