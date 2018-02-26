from itertools import product

from adversarial_search import Game
from adversarial_search import Max
from .action import Action
from .game_state import GameState

DIMENSION = 4


class NumericalTicTacToe(Game):
    def __init__(self):
        initial_state = self.get_initial_state()
        super().__init__(initial_state)

    @classmethod
    def get_initial_state(cls):
        board = cls.get_initial_board()
        initial_player = Max
        return GameState(board, initial_player)

    @classmethod
    def get_initial_board(cls):
        coordinates = cls.get_board_coordinates()
        return {coordinate: 0 for coordinate in coordinates}

    @staticmethod
    def get_board_coordinates():
        """Get a list of tuples representing board coordinates.

        [(0, 0), (0, 1), (0, 2), ..., (3, 1), (3, 2), (3, 3)]
        """
        return list(product(range(DIMENSION), repeat=2))

    def player(self, state):
        return state.current_player

    def actions(self, state):
        super().actions(state)

    @classmethod
    def possible_actions(cls, player):
        """Return a player's possible actions.

        Possibles actions are a list of tuples in the form of ((x,  y), value),
        where (x, y) is a board position, and value is the numerical move.
        :param player:
        :return: Possible actions.
        """
        coordinates = cls.get_board_coordinates()
        return [Action(c, v) for v in cls.possible_values(player) for c in coordinates]

    @staticmethod
    def possible_values(player):
        """Return a player's possible values."""
        if player.is_max():
            return {1, 3, 5, 7, 9, 11, 13, 15}
        else:
            return {2, 4, 6, 8, 10, 12, 14, 16}

    def result(self, state, action):
        super().result(state, action)

    def terminal_test(self, state):
        super().terminal_test(state)

    def utility(self, state, player):
        super().utility(state, player)
