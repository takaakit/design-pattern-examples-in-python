#!/usr/bin/env python
# -*- coding: utf-8 -*-

from behavioral_patterns.strategy.game_result_type import GameResultType
from behavioral_patterns.strategy.player import Player
from behavioral_patterns.strategy.mirror_strategy import MirrorStrategy
from behavioral_patterns.strategy.random_strategy import RandomStrategy

'''
A game of rock-scissors-paper. Two strategies are available:
* Random Strategy: showing a random hand signal.
* Mirror Strategy: showing a hand signal from the previous opponent's hand signal.
'''

if __name__ == '__main__':
    player_1 = Player('Emily', RandomStrategy())
    player_2 = Player('James', MirrorStrategy())

    for i in range(100):
        hand_of_player_1 = player_1.show_hand_signal()
        hand_of_player_2 = player_2.show_hand_signal()

        # Judge win, loss, or draw
        result_of_player_1: GameResultType
        result_of_player_2: GameResultType
        if hand_of_player_1.is_stronger_than(hand_of_player_2):
            print('Winner: ' + player_1.to_string())
            result_of_player_1 = GameResultType.WIN
            result_of_player_2 = GameResultType.LOSS
        elif hand_of_player_2.is_stronger_than(hand_of_player_1):
            print('Winner: ' + player_2.to_string())
            result_of_player_1 = GameResultType.LOSS
            result_of_player_2 = GameResultType.WIN
        else:
            print('Draw...')
            result_of_player_1 = GameResultType.DRAW
            result_of_player_2 = GameResultType.DRAW

        player_1.notify_game_result(result_of_player_1, hand_of_player_1, hand_of_player_2)
        player_2.notify_game_result(result_of_player_2, hand_of_player_2, hand_of_player_1)

    print('RESULT:')
    print(player_1.to_string())
    print(player_2.to_string())
