"""
A computer numerical tic-tac-toe player.

References:
Artificial Intelligence: A Modern Approach (3rd Edition) by Stuart J. Russel and Peter Norvig
Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
"""

from adversarial_search import Minimax
from numerical_tic_tac_toe import Action
from numerical_tic_tac_toe import Max
from numerical_tic_tac_toe import Min
from numerical_tic_tac_toe import NumericalTicTacToe


def main():
    game = NumericalTicTacToe(dimension=3)
    players = [Max, Min]
    state = game.initial_state
    print(state)
    while True:
        for player in players:
            if player.is_max():
                position = int(input('Enter a position (0 - 15): '))
                number = int(input('Enter a number: '))
                coordinate = game.map_position_to_coordinate(position)
                action = Action(coordinate, number)
            else:
                action = Minimax.decision(state, game)
            state = game.result(state, action)
            print(state)
            if game.terminal_test(state):
                print("Game over!")
                return game.utility(state, player)


if __name__ == '__main__':
    main()
