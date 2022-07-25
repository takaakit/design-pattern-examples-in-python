#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from structural_patterns.adapter.message_display import MessageDisplay
from structural_patterns.adapter.print import Print

# ˄


# Adapt the MessageDisplay interface to the Print interface.
class PrintMessageDisplay(MessageDisplay, Print):
    # ˅

    # ˄

    def __init__(self, message):
        # ˅
        super().__init__(message)
        # ˄

    def print_weak(self):
        # ˅
        self.display_with_hyphens()
        # ˄

    def print_strong(self):
        # ˅
        self.display_with_brackets()
        # ˄

    # ˅

    # ˄


# ˅

# ˄
