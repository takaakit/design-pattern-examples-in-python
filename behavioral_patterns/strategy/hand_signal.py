#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class HandSignal(object):
    # ˅
    
    # ˄

    ROCK = 0

    SCISSORS = 1

    PAPER = 2

    # Characters of the hands
    name = ['Rock', 'Scissors', 'Paper']

    def __init__(self, value):

        # Values of rock, scissors and paper.
        self.value = value

        # ˅
        pass
        # ˄

    # Return true if "this" is stronger than "hand".
    def is_stronger_than(self, hand):
        # ˅
        return self.__judge_game(hand) == 1
        # ˄

    # Return false if "this" is weaker than "hand".
    def is_weaker_than(self, hand):
        # ˅
        return self.__judge_game(hand) == -1
        # ˄

    def __str__(self):
        # ˅
        return self.name[self.value]
        # ˄

    # The draw is 0. "this" win is 1. "hand" win is -1.
    def __judge_game(self, hand):
        # ˅
        if self.value == hand.value:
            return 0
        elif (self.value + 1) % 3 == hand.value:
            return 1
        else:
            return -1
        # ˄

    # ˅
    
    # ˄


# ˅

# Characters of the hands
hands = [HandSignal(HandSignal.ROCK), HandSignal(HandSignal.SCISSORS), HandSignal(HandSignal.PAPER)]


# Get an instance of the hand
def get_hand(hand_value):
    return hands[hand_value]

# ˄
