import unittest

from numerical_tic_tac_toe import Action
from numerical_tic_tac_toe import GameState
from numerical_tic_tac_toe import Max
from numerical_tic_tac_toe import Min
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

    def test_actions_for_max(self):
        expected_actions = [Action((1, 0), 3), Action((2, 3), 3)]
        nearly_complete_board = get_nearly_complete_board()
        player = Max
        state = GameState(nearly_complete_board, player)
        game = NumericalTicTacToe()
        actions = game.actions(state)

        self.assertEqual(expected_actions, actions)

    def test_actions_for_min(self):
        expected_actions = [Action((1, 0), 2), Action((2, 3), 2)]
        nearly_complete_board = get_nearly_complete_board()
        player = Min
        state = GameState(nearly_complete_board, player)
        game = NumericalTicTacToe()
        actions = game.actions(state)

        self.assertEqual(expected_actions, actions)


def get_nearly_complete_board():
    return {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
            (1, 0): 0, (1, 1): 13, (1, 2): 11, (1, 3): 14,
            (2, 0): 1, (2, 1): 9, (2, 2): 15, (2, 3): 0,
            (3, 0): 5, (3, 1): 4, (3, 2): 7, (3, 3): 8}


if __name__ == '__main__':
    unittest.main()
