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


# Calculate a hand from the previous hand stochastically.
class StrategyB(Strategy):
    # ˅

    # ˄

    def __init__(self, random_seed):

        self.__history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

        self.__pre_hand = get_hand(ROCK)

        self.__cur_hand = get_hand(ROCK)

        # ˅
        pass
        # ˄

    def next_hand(self):
        # ˅
        random_hand_value = random.randrange(self.__get_history_sum(self.__cur_hand.value))
        hand_value = 0
        if random_hand_value < self.__history[self.__cur_hand.value][0]:
            hand_value = ROCK
        elif random_hand_value < self.__history[self.__cur_hand.value][0] + self.__history[self.__cur_hand.value][1]:
            hand_value = SCISSORS
        else:
            hand_value = PAPER
        self.__pre_hand = self.__cur_hand
        self.__cur_hand = get_hand(hand_value)
        return self.__cur_hand
        # ˄

    def learn(self, win):
        # ˅
        if win:
            self.__history[self.__pre_hand.value][self.__cur_hand.value] += 1
        else:
            self.__history[self.__pre_hand.value][(self.__cur_hand.value + 1) % 3] += 1
            self.__history[self.__pre_hand.value][(self.__cur_hand.value + 2) % 3] += 1
        # ˄

    def __get_history_sum(self, hand_value):
        # ˅
        sum = 0
        for i in range(2):
            sum += self.__history[hand_value][i]
        return sum
        # ˄

    # ˅

    # ˄


# ˅

# ˄
