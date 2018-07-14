#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅

# ˄


class Hand(object):
    # ˅

    # ˄

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

    def to_string(self):
        # ˅
        return name[self.value]
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

# Hands of rock-scissors-paper
ROCK = 0        # Rock
SCISSORS = 1    # Scissors
PAPER = 2       # Paper

# Characters of the hands
hands = [Hand(ROCK), Hand(SCISSORS), Hand(PAPER)]

# Characters of the hands
name = ['Rock', 'Scissors', 'Paper']

# Get an instance of the hand
def get_hand(hand_value):
    return hands[hand_value]

# ˄
