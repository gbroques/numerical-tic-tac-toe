import unittest

from adversarial_search import Max
from adversarial_search import Min
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

    def test_possible_actions_for_max(self):
        expected_possible_actions_for_max = {1, 3, 5, 7, 9, 11, 13, 15}
        game = NumericalTicTacToe()
        possible_actions_for_max = game.possible_actions(Max)

        self.assertEqual(expected_possible_actions_for_max, possible_actions_for_max)

    def test_possible_actions_for_min(self):
        expected_possible_actions_for_min = {2, 4, 6, 8, 10, 12, 14, 16}
        game = NumericalTicTacToe()
        possible_actions_for_min = game.possible_actions(Min)

        self.assertEqual(expected_possible_actions_for_min, possible_actions_for_min)


if __name__ == '__main__':
    unittest.main()
