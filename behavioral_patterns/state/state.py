#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class State(object, metaclass=ABCMeta):
    # ˅

    # ˄

    @abstractmethod
    def set_time(self, context, hour):
        # ˅
        pass
        # ˄

    @abstractmethod
    def use(self, context):
        # ˅
        pass
        # ˄

    @abstractmethod
    def alarm(self, context):
        # ˅
        pass
        # ˄

    @abstractmethod
    def phone(self, context):
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
