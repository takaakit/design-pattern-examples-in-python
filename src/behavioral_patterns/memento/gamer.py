#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ˅
import random
from behavioral_patterns.memento.memento import Memento

# ˄


class Gamer(object):
    # ˅
    
    # ˄

    def __init__(self, money):

        # Gamer's money
        self.money = money

        # Acquired desserts 
        self.__desserts = []

        # Dessert name table
        self.__desserts_name = ['Cake', 'Candy', 'Cookie']

        # ˅
        pass
        # ˄

    # Get current status
    def create_memento(self):
        # ˅
        memento = Memento(self.money)
        it_desserts = iter(self.__desserts)
        for it in it_desserts:
            memento.add_dessert(it)
        return memento
        # ˄

    # Undo status
    def restore_memento(self, memento):
        # ˅
        self.money = memento.money
        self.__desserts = memento.desserts
        # ˄

    # Play a game
    def play(self):
        # ˅
        dice = random.randrange(1, 6, 1)
        # In case of 1...Gamer's money increases
        if dice == 1:
            self.money += 100
            print('Gamer\'s money increases.')
        # In case of 2...Gamer's money halves
        elif dice == 2:
            self.money /= 2
            print('Gamer\'s money halves.')
        # In case of 6...Gamer gets desserts
        elif dice == 6:
            got_dessert = self.__get_dessert()
            print('Gamer gets desserts(' + got_dessert + ')')
            self.__desserts.append(got_dessert)
        # Other...Nothing happens
        else:
            print('Nothing happens.')
        # ˄

    def to_string(self):
        # ˅
        return '[money = ' + str(self.money) + ', desserts = ' + self.__desserts.__str__() + ']'
        # ˄

    # Get a dessert
    def __get_dessert(self):
        # ˅
        prefix = ''
        if random.randrange(0, 2, 1):
            prefix = 'Delicious '
        return prefix + self.__desserts_name[random.randrange(0, 2, 1)]
        # ˄

    # ˅
    
    # ˄


# ˅

# ˄
