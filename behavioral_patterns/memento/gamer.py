#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
import sys

from behavioral_patterns.memento.memento import Memento

# ˄


class Gamer(object):
    # ˅
    
    # ˄

    def __init__(self, money):

        # Gamer's money
        self.__money = money

        # ˅
        pass
        # ˄

    def create_memento(self):
        # ˅
        memento = Memento(self.__money)
        return memento
        # ˄

    def set_memento(self, memento):
        # ˅
        self.__money = memento.money
        # ˄

    # Play a game
    def play(self):
        # ˅
        dice = random.randrange(1, 6, 1)    # Shake a dice

        pre_money = self.__money
        if dice == 1 or dice == 3 or dice == 5:
            # In case of odd...Money is halved
            self.__money = int(self.__money / 2)
            print('Gamer\'s money is halved: ' + str(pre_money) + ' -> ' + str(self.__money))
        elif dice == 2 or dice == 4 or dice == 6:
            # In case of even...Money doubles
            self.__money = int(self.__money * 2)
            print('Gamer\'s money doubles: ' + str(pre_money) + ' -> ' + str(self.__money))
        else:
            # Other...Exit
            print('Unexpected value.')
            sys.exit(1)
        # ˄

    def to_string(self):
        # ˅
        return '[money = ' + str(self.__money) + ']'
        # ˄

    @property
    def money(self):
        # ˅
        return self.__money
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
