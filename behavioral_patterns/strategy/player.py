#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
from behavioral_patterns.strategy.game_result_type import GameResultType

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

    # Show a hand signal from the strategy.
    def show_hand_signal(self):
        # ˅
        return self.__strategy.show_hand_signal()
        # ˄

    # Notify a game result.
    def notify_game_result(self, result, own_hand, opponents_hand):
        # ˅
        if result == GameResultType.WIN:
            self.__win_count += 1
            self.__game_count += 1
        elif result == GameResultType.LOSS:
            self.__loss_count += 1
            self.__game_count += 1
        elif result == GameResultType.DRAW:
            self.__game_count += 1

        self.__strategy.notify_game_result(result, own_hand, opponents_hand)
        # ˄

    def to_string(self):
        # ˅
        return self.__name + ' [' + str(self.__game_count) + ' games, ' + str(self.__win_count) + ' won, ' + str(self.__loss_count) + ' lost, ' + str(self.__game_count - self.__win_count - self.__loss_count) + ' drew]'
        # ˄

    # ˅

    # ˄


# ˅

# ˄
