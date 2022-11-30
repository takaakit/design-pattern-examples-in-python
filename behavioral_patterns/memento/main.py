#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from behavioral_patterns.memento.gamer import Gamer

'''
A dice game in which money increases and decreases:
* A gamer shakes a dice and the number determine the next state.
* If the number of dice is even, gamer's money doubles, and if it is odd, gamer's money is halved.
* If the gamer's money is less than half of the highest amount, it returns to the highest amount.
* The game is repeated.
'''

if __name__ == '__main__':
    gamer = Gamer(money=100)                # The initial money is 100
    memento = gamer.create_memento()        # Save the initial state

    for i in range(0, 10):
        print(f'==== Turn {i + 1}')         # Display count

        gamer.play()                        # Play a game

        # Determine the behavior of the Memento
        if gamer.money > memento.money:
            print('(Gamers\' money is the highest ever, so record the current state.)')
            memento = gamer.create_memento()
        elif gamer.money < memento.money / 2:
            print('(Gamer\'s money is less than half of the highest amount, so return to the recorded state.)')
            gamer.set_memento(memento)
            print(f'Gamer\'s money returns to {gamer.money}.')

        print('')

        sleep(1)

