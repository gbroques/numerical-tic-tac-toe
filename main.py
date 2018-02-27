"""
A computer numerical tic-tac-toe player.

References:
Artificial Intelligence: A Modern Approach (3rd Edition) by Stuart J. Russel and Peter Norvig
Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
"""

from itertools import product

from adversarial_search import minimax_decision
from numerical_tic_tac_toe import Action
from numerical_tic_tac_toe import Max
from numerical_tic_tac_toe import Min
from numerical_tic_tac_toe import NumericalTicTacToe


def map_position_to_coordinate(position):
    # TODO: remove duplication
    board_coordinates = list(product(range(4), repeat=2))
    return board_coordinates[position]


def main():
    game = NumericalTicTacToe()
    players = [Max, Min]
    state = game.initial_state
    print(state)
    while True:
        for player in players:
            position = int(input('Enter a position (0 - 15): '))
            number = int(input('Enter a number: '))
            coordinate = map_position_to_coordinate(position)
            action = Action(coordinate, number)
            state = game.result(state, action)
            print(state)
            if game.terminal_test(state):
                print("Game over!")
                return game.utility(state, player)


if __name__ == '__main__':
    main()
