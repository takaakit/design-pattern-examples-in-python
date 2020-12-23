#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from abc import *

# ˄


class Strategy(object, metaclass=ABCMeta):
    # ˅
    
    # ˄

    # Show a hand signal.
    @abstractmethod
    def show_hand_signal(self):
        # ˅
        pass
        # ˄

    # Notify a game result.
    @abstractmethod
    def notify_game_result(self, result, own_hand, opponents_hand):
        # ˅
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
