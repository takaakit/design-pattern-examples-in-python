#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from behavioral_patterns.strategy.player import Player
from behavioral_patterns.strategy.strategy_a import StrategyA
from behavioral_patterns.strategy.strategy_b import StrategyB

"""
A game of rock-scissors-paper.
There are two strategies below.

* When winning a game, show the same hand at the next time.
* Calculate a hand from the previous hand stochastically.
"""

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print('Usage: python main.py RandomSeedNumber1 RandomSeedNumber2')
        print('Ex.  : python main.py 314 15')
    else:
        random_seed_1 = int(args[1])
        random_seed_2 = int(args[2])
        player_1 = Player('Emily', StrategyA(random_seed_1))
        player_2 = Player('James', StrategyB(random_seed_2))

        for i in range(100):
            next_hand_1 = player_1.next_hand()
            next_hand_2 = player_2.next_hand()
            if next_hand_1.is_stronger_than(next_hand_2):
                print('Winner: ' + player_1.to_string())
                player_1.won()
                player_2.lost()
            elif next_hand_2.is_stronger_than(next_hand_1):
                print('Winner: ' + player_2.to_string())
                player_1.lost()
                player_2.won()
            else:
                print('Draw...')
                player_1.drew()
                player_2.drew()
        print('RESULT:')
        print(player_1.to_string())
        print(player_2.to_string())
