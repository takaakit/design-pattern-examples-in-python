#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.strategy.hand_signal import get_hand, HandSignal
from behavioral_patterns.strategy.strategy import Strategy

# ˄


# Mirror Strategy: showing a hand signal from the previous opponent's hand signal.
class MirrorStrategy(Strategy):
    # ˅
    
    # ˄

    def __init__(self):

        self.__pre_opponents_hand = get_hand(HandSignal.ROCK)

        # ˅
        pass
        # ˄

    def show_hand_signal(self):
        # ˅
        return self.__pre_opponents_hand
        # ˄

    def notify_game_result(self, result, own_hand, opponents_hand):
        # ˅
        self.__pre_opponents_hand = opponents_hand
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
