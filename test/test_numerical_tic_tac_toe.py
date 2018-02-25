import unittest

from adversarial_search import Max
from numerical_tic_tac_toe import GameState
from numerical_tic_tac_toe import NumericalTicTacToe


class TestNumericalTicTacToe(unittest.TestCase):

    def test_initial_state(self):
        expected_initial_board = [[0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0],
                                  [0, 0, 0, 0]]
        expected_initial_player = Max

        expected_initial_state = GameState(expected_initial_board,
                                           expected_initial_player)

        game = NumericalTicTacToe()
        self.assertEqual(expected_initial_state, game.get_initial_state())

    def test_player(self):
        expected_player = Max
        game = NumericalTicTacToe()
        state = game.get_initial_state()
        self.assertEqual(expected_player, game.player(state))


if __name__ == '__main__':
    unittest.main()
