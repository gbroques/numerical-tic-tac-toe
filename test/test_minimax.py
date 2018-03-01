import unittest

from adversarial_search import Game
from adversarial_search import Minimax


class TestMinimax(unittest.TestCase):
    def test_minimax(self):
        expected_decision = 'a1'

        game = SimpleGame()
        decision = Minimax.decision(game.initial_state, game)

        self.assertEqual(expected_decision, decision)


class SimpleGame(Game):
    """The game serves as a simple test case for minimax.

    Source:
    https://github.com/aimacode/aima-python/blob/master/games.py

    Reference:
    Artificial Intelligence: A Modern Approach (3rd Edition)
    Figure 5.2, Page 164
    """

    successors = dict(A=dict(a1='B', a2='C', a3='D'),
                      B=dict(b1='B1', b2='B2', b3='B3'),
                      C=dict(c1='C1', c2='C2', c3='C3'),
                      D=dict(d1='D1', d2='D2', d3='D3'))
    utilities = dict(B1=3, B2=12, B3=8, C1=2, C2=4, C3=6, D1=14, D2=5, D3=2)
    initial_state = 'A'

    def __init__(self):
        super().__init__(self.initial_state)

    def actions(self, state):
        return list(self.successors.get(state, {}).keys())

    def result(self, state, move):
        return self.successors[state][move]

    def utility(self, state, player):
        if player == 'MAX':
            return self.utilities[state]
        else:
            return -self.utilities[state]

    def terminal_test(self, state):
        return state not in ('A', 'B', 'C', 'D')

    def player(self, state):
        return 'MIN' if state in 'BCD' else 'MAX'
