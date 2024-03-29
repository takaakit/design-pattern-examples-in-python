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
        memento = Memento(money=self.__money)
        return memento
        # ˄

    def set_memento(self, memento):
        # ˅
        self.__money = memento.money
        # ˄

    # Play a game
    def play(self):
        # ˅
        dice = random.randrange(start=1, stop=6, step=1)    # Shake a dice
        print(f'The number of dice is {dice}.')
        pre_money = self.__money
        if dice == 1 or dice == 3 or dice == 5:
            # In case of odd...Money is halved
            self.__money = int(self.__money / 2)
            print(f'Gamer\'s money is halved: {pre_money} -> {self.__money}')
        elif dice == 2 or dice == 4 or dice == 6:
            # In case of even...Money doubles
            self.__money = int(self.__money * 2)
            print(f'Gamer\'s money doubles: {pre_money} -> {self.__money}')
        else:
            # Other...Exit
            exit('ERROR: Unexpected value.')
        # ˄

    def to_string(self):
        # ˅
        return f'[money = {self.__money}]'
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
