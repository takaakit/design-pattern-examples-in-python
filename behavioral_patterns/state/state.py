#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class State(object, metaclass=ABCMeta):
    # ˅

    # ˄

    # Set time
    @abstractmethod
    def set_time(self, context, hour):
        # ˅
        pass
        # ˄

    # Use a safe
    @abstractmethod
    def use_safe(self, context):
        # ˅
        pass
        # ˄

    # Sound a emergency bell
    @abstractmethod
    def sound_bell(self, context):
        # ˅
        pass
        # ˄

    # Make a normal call
    @abstractmethod
    def call(self, context):
        # ˅
        pass
        # ˄

    @abstractmethod
    def to_string(self):
        # ˅
        pass
        # ˄

    # ˅

    # ˄


# ˅

# ˄
