"""
A computer numerical tic-tac-toe player.

References:
Artificial Intelligence: A Modern Approach (3rd Edition) by Stuart J. Russel and Peter Norvig
Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
"""

from numerical_tic_tac_toe import NumericalTicTacToe


def main():
    game = NumericalTicTacToe(dimension=4)
    result = game.play()
    if result == 'draw':
        print("It's a draw!")
    else:
        print(str(result()) + " wins!")


if __name__ == '__main__':
    main()
