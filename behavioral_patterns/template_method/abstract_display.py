#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class AbstractDisplay(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def open(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def write(self):
        # ˅
        pass
        # ˄

    @abstractmethod
    def close(self):
        # ˅
        pass
        # ˄

    def output(self):
        # ˅
        self.open()
        for _ in range(5):      # Repeat write 5 times
            self.write()
        self.close()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
