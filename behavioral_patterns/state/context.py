#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Context(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    # Set time
    @abstractmethod
    def set_time(self, hour):
        # ˅
        pass
        # ˄

    # Change state
    @abstractmethod
    def change_state(self, state):
        # ˅
        pass
        # ˄

    # Call a security guard room
    @abstractmethod
    def call_security_guards_room(self, msg):
        # ˅
        pass
        # ˄

    # Record security log
    @abstractmethod
    def record_security_log(self, msg):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
