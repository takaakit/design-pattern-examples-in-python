#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.bridge.display import Display

# ˄


class MultiLineDisplay(Display):
    # ˅

    # ˄

    def __init__(self, impl):
        # ˅
        super().__init__(impl)
        # ˄

    # Repeat display for the specified number of times
    def output_multiple(self, times):
        # ˅
        self.open()
        for i in range(times):
            self.write()
        self.close()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
