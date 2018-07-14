#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.strategy.strategy import Strategy

# ˄


class Player(object):
    # ˅

    # ˄

    def __init__(self, name, strategy):

        self.__name = name

        self.__win_count = 0

        self.__loss_count = 0

        self.__game_count = 0

        self.__strategy = strategy

        # ˅
        pass
        # ˄

    # Calculate a hand from the strategy.
    def next_hand(self):
        # ˅
        return self.__strategy.next_hand()
        # ˄

    # Won a game.
    def won(self):
        # ˅
        self.__strategy.learn(True)
        self.__win_count += 1
        self.__game_count += 1
        # ˄

    # Lost a game.
    def lost(self):
        # ˅
        self.__strategy.learn(False)
        self.__loss_count += 1
        self.__game_count += 1
        # ˄

    # Drew a game.
    def drew(self):
        # ˅
        self.__game_count += 1
        # ˄

    def to_string(self):
        # ˅
        return self.__name + ' [' + str(self.__game_count) + ' games, ' + str(self.__win_count) + ' won, ' + str(self.__loss_count) + ' lost, ' + str(self.__game_count - self.__win_count - self.__loss_count) + ' drew]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
