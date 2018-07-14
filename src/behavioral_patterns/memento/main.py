#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from behavioral_patterns.memento.gamer import Gamer

"""
Dice game collecting fruits.

* A gamer shakes a dice and the number determine the next state.
* Gamer's money increases or decreases depending on the number. The gamer sometimes gets desserts.
* The game is over if the gamer's money runs out.
"""

if __name__ == '__main__':
    gamer = Gamer(100)
    memento = gamer.create_memento()

    for i in range(0, 99, 1):
        print('==== ' + str(i))
        print('Current state: ' + gamer.to_string())

        gamer.play()

        print('Gamer\'s money is ' + str(gamer.money) + '.')

        if gamer.money > memento.money:
            print('(Save the current state because money has increased.)')
            memento = gamer.create_memento()
        elif gamer.money < memento.money / 2:
            print('(Go back to the previous state because money has decreased.)')
            gamer.restore_memento(memento)

        sleep(1)

        print('')
