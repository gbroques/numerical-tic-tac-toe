from adversarial_search import Game
from adversarial_search import Max
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

    @staticmethod
    def get_initial_board():
        return [[0] * DIMENSION for _ in range(DIMENSION)]

    def player(self, state):
        super().player(state)

    def actions(self, state):
        super().actions(state)

    def result(self, state, action):
        super().result(state, action)

    def terminal_test(self, state):
        super().terminal_test(state)

    def utility(self, state, player):
        super().utility(state, player)
