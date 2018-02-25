from adversarial_search import Game
from .state import State

DIMENSION = 4


class NumericalTicTacToe(Game):
    def __init__(self):
        initial_state = self.get_initial_state()
        super().__init__(initial_state)

    @staticmethod
    def get_initial_state():
        return State([[0] * DIMENSION for _ in range(DIMENSION)])

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
