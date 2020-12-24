#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.strategy.hand_signal import get_hand
from behavioral_patterns.strategy.strategy import Strategy

# ˄


# Random Strategy: showing a random hand signal.
class RandomStrategy(Strategy):
    # ˅
    
    # ˄

    def __init__(self):
        # ˅
        pass
        # ˄

    def show_hand_signal(self):
        # ˅
        return get_hand(random.randrange(3))
        # ˄

    def notify_game_result(self, result, own_hand, opponents_hand):
        # ˅
        # Do nothing
        pass
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
