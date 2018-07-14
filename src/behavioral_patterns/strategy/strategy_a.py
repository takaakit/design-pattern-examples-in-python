#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.strategy.hand import Hand
from behavioral_patterns.strategy.hand import get_hand
from behavioral_patterns.strategy.hand import ROCK
from behavioral_patterns.strategy.hand import SCISSORS
from behavioral_patterns.strategy.hand import PAPER
from behavioral_patterns.strategy.strategy import Strategy

# ˄


# When winning a game, show the same hand at the next time.
class StrategyA(Strategy):
    # ˅

    # ˄

    def __init__(self, random_seed):

        self.__won = False

        self.__pre_hand = get_hand(ROCK)

        # ˅
        pass
        # ˄

    def next_hand(self):
        # ˅
        if self.__won == False:
            self.__pre_hand = get_hand(random.randrange(0, 3, 1))
        return self.__pre_hand
        # ˄

    def learn(self, win):
        # ˅
        self.__won = win
        # ˄

    # ˅

    # ˄


# ˅

# ˄
