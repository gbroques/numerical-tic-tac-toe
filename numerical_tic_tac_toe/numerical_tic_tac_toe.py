from adversarial_search.game import Game


class NumericalTicTacToe(Game):
    def __init__(self, initial_state):
        super().__init__(initial_state)

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
