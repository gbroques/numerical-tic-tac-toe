import unittest

from adversarial_search import Max
from adversarial_search import Min
from numerical_tic_tac_toe import Action
from numerical_tic_tac_toe import GameState
from numerical_tic_tac_toe import NumericalTicTacToe


class TestNumericalTicTacToe(unittest.TestCase):

    def test_initial_state(self):
        expected_initial_state = self.get_expected_initial_state()

        game = NumericalTicTacToe()

        self.assertEqual(expected_initial_state, game.get_initial_state())

    def get_expected_initial_state(self):
        expected_initial_board = self.get_expected_initial_board()
        expected_initial_player = Max
        return GameState(expected_initial_board, expected_initial_player)

    @staticmethod
    def get_expected_initial_board():
        return {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
                (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0,
                (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
                (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}

    def test_player(self):
        expected_player = Max
        game = NumericalTicTacToe()
        state = game.get_initial_state()
        self.assertEqual(expected_player, game.player(state))

    def test_possible_values_for_max(self):
        expected_possible_values_for_max = {1, 3, 5, 7, 9, 11, 13, 15}
        game = NumericalTicTacToe()
        possible_values_for_max = game.possible_values(Max)

        self.assertEqual(expected_possible_values_for_max, possible_values_for_max)

    def test_possible_values_for_min(self):
        expected_possible_values_for_min = {2, 4, 6, 8, 10, 12, 14, 16}
        game = NumericalTicTacToe()
        possible_values_for_min = game.possible_values(Min)

        self.assertEqual(expected_possible_values_for_min, possible_values_for_min)

    def test_possible_actions_for_max(self):
        expected_num_actions = 128

        game = NumericalTicTacToe()
        possible_actions = game.possible_actions(Max)

        self.assertEqual(expected_num_actions, len(possible_actions))
        self.assertIn(Action((0, 0), 1), possible_actions)
        self.assertIn(Action((0, 3), 9), possible_actions)
        self.assertIn(Action((2, 2), 11), possible_actions)
        self.assertNotIn(Action((-1, 0), 1), possible_actions)
        self.assertNotIn(Action((4, 0), 1), possible_actions)
        self.assertNotIn(Action((3, 0), 2), possible_actions)

    def test_possible_actions_for_min(self):
        expected_num_actions = 128

        game = NumericalTicTacToe()
        possible_actions = game.possible_actions(Min)

        self.assertEqual(expected_num_actions, len(possible_actions))
        self.assertIn(Action((1, 2), 2), possible_actions)
        self.assertIn(Action((3, 3), 8), possible_actions)
        self.assertIn(Action((0, 1), 12), possible_actions)
        self.assertNotIn(Action((-1, 0), 4), possible_actions)
        self.assertNotIn(Action((4, 0), 8), possible_actions)
        self.assertNotIn(Action((3, 0), 1), possible_actions)


if __name__ == '__main__':
    unittest.main()
