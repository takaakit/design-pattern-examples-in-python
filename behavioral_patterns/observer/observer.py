#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


# Defines an updating interface for objects that should be notified of changes in a subject.
class Observer(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    @abstractmethod
    def update(self, changedSubject):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
