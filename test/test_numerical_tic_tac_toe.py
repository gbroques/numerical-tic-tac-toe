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

    def test_possible_actions_for_min_with_dimension_two(self):
        expected_num_actions = 8

        game = NumericalTicTacToe(dimension=2)
        possible_actions = game.possible_actions(Min)

        self.assertEqual(expected_num_actions, len(possible_actions))
        self.assertIn(Action((0, 1), 4), possible_actions)
        self.assertIn(Action((1, 0), 2), possible_actions)
        self.assertIn(Action((1, 1), 4), possible_actions)
        self.assertNotIn(Action((-1, 0), 1), possible_actions)
        self.assertNotIn(Action((0, 0), 1), possible_actions)
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

    def test_result(self):
        expected_next_state = self.get_expected_next_state()
        nearly_complete_board = get_nearly_complete_board()
        state = GameState(nearly_complete_board, Max)
        game = NumericalTicTacToe()
        next_state = game.result(state, Action((1, 0), 3))

        self.assertEqual(expected_next_state, next_state)

    @staticmethod
    def get_expected_next_state():
        board = {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
                 (1, 0): 3, (1, 1): 13, (1, 2): 11, (1, 3): 14,
                 (2, 0): 1, (2, 1): 9, (2, 2): 15, (2, 3): 0,
                 (3, 0): 5, (3, 1): 4, (3, 2): 7, (3, 3): 8}
        player = Min
        return GameState(board, player)

    def test_is_win_with_dimension_four(self):
        vertical_win = {(0, 0): 0, (0, 1): 0, (0, 2): 12, (0, 3): 0,
                        (1, 0): 0, (1, 1): 0, (1, 2): 13, (1, 3): 0,
                        (2, 0): 0, (2, 1): 15, (2, 2): 5, (2, 3): 0,
                        (3, 0): 0, (3, 1): 0, (3, 2): 4, (3, 3): 0}

        horizontal_win = {(0, 0): 0, (0, 1): 0, (0, 2): 7, (0, 3): 0,
                          (1, 0): 12, (1, 1): 5, (1, 2): 4, (1, 3): 13,
                          (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
                          (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}

        major_diagonal_win = {(0, 0): 12, (0, 1): 0, (0, 2): 0, (0, 3): 15,
                              (1, 0): 0, (1, 1): 5, (1, 2): 0, (1, 3): 0,
                              (2, 0): 0, (2, 1): 0, (2, 2): 4, (2, 3): 0,
                              (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 13}
        game = NumericalTicTacToe(dimension=4)
        self.assertTrue(game.is_win(vertical_win))
        self.assertTrue(game.is_win(horizontal_win))
        self.assertTrue(game.is_win(major_diagonal_win))

    def test_is_win_with_dimension_three(self):
        not_horizontal_win = {(0, 0): 8, (0, 1): 0, (0, 2): 7,
                              (1, 0): 0, (1, 1): 0, (1, 2): 0,
                              (2, 0): 0, (2, 1): 0, (2, 2): 0}

        not_diagonal_win = {(0, 0): 8, (0, 1): 0, (0, 2): 0,
                            (1, 0): 0, (1, 1): 0, (1, 2): 0,
                            (2, 0): 0, (2, 1): 0, (2, 2): 7}
        game = NumericalTicTacToe(dimension=3)

        self.assertFalse(game.is_win(not_horizontal_win))
        self.assertFalse(game.is_win(not_diagonal_win))

    def test_is_win_with_dimension_two(self):
        vertical_win = {(0, 0): 2, (0, 1): 3,
                        (1, 0): 1, (1, 1): 0}

        horizontal_win = {(0, 0): 0, (0, 1): 2,
                          (1, 0): 1, (1, 1): 3}

        minor_diagonal_win = {(0, 0): 1, (0, 1): 2,
                              (1, 0): 3, (1, 1): 0}

        game = NumericalTicTacToe(dimension=2)
        self.assertTrue(game.is_win(vertical_win))
        self.assertTrue(game.is_win(horizontal_win))
        self.assertTrue(game.is_win(minor_diagonal_win))

    def test_utility_with_full_board(self):
        expected_utility = 0
        full_board = {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
                      (1, 0): 3, (1, 1): 13, (1, 2): 11, (1, 3): 14,
                      (2, 0): 1, (2, 1): 9, (2, 2): 15, (2, 3): 2,
                      (3, 0): 5, (3, 1): 4, (3, 2): 7, (3, 3): 8}

        game = NumericalTicTacToe()
        utility = game.utility(GameState(full_board, Min), Max)

        self.assertEqual(expected_utility, utility)

    def test_utility_with_max_winning(self):
        expected_utility = 1

        board = {(0, 0): 0, (0, 1): 0, (0, 2): 12, (0, 3): 0,
                 (1, 0): 0, (1, 1): 0, (1, 2): 13, (1, 3): 0,
                 (2, 0): 0, (2, 1): 15, (2, 2): 5, (2, 3): 0,
                 (3, 0): 0, (3, 1): 0, (3, 2): 4, (3, 3): 0}
        game = NumericalTicTacToe()
        utility = game.utility(GameState(board, Min), Max)

        self.assertEqual(expected_utility, utility)

    def test_utility_with_min_winning(self):
        expected_utility = -1

        winning_board = {(0, 0): 0, (0, 1): 0, (0, 2): 12, (0, 3): 0,
                         (1, 0): 0, (1, 1): 0, (1, 2): 13, (1, 3): 0,
                         (2, 0): 0, (2, 1): 0, (2, 2): 5, (2, 3): 0,
                         (3, 0): 0, (3, 1): 0, (3, 2): 4, (3, 3): 0}
        game = NumericalTicTacToe()
        utility = game.utility(GameState(winning_board, Max), Min)

        self.assertEqual(expected_utility, utility)

    def test_terminal_state_with_full_board(self):
        full_board = {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
                      (1, 0): 3, (1, 1): 13, (1, 2): 11, (1, 3): 14,
                      (2, 0): 1, (2, 1): 9, (2, 2): 15, (2, 3): 2,
                      (3, 0): 5, (3, 1): 4, (3, 2): 7, (3, 3): 8}

        game = NumericalTicTacToe()
        is_over = game.terminal_test(GameState(full_board, Min))

        self.assertTrue(is_over)

    def test_terminal_test_with_max_winning(self):
        winning_board = {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
                         (1, 0): 3, (1, 1): 11, (1, 2): 13, (1, 3): 0,
                         (2, 0): 0, (2, 1): 9, (2, 2): 5, (2, 3): 2,
                         (3, 0): 15, (3, 1): 7, (3, 2): 4, (3, 3): 8}
        game = NumericalTicTacToe()
        is_over = game.terminal_test(GameState(winning_board, Min))

        self.assertTrue(is_over)

    def test_terminal_test_with_min_winning(self):
        winning_board = {(0, 0): 0, (0, 1): 0, (0, 2): 12, (0, 3): 0,
                         (1, 0): 0, (1, 1): 0, (1, 2): 13, (1, 3): 0,
                         (2, 0): 0, (2, 1): 0, (2, 2): 5, (2, 3): 0,
                         (3, 0): 0, (3, 1): 0, (3, 2): 4, (3, 3): 0}
        game = NumericalTicTacToe()
        is_over = game.terminal_test(GameState(winning_board, Max))

        self.assertTrue(is_over)

    def test_get_possible_numbers_for_dimension_two(self):
        expected_possible_numbers_for_max = {1, 3}
        expected_possible_numbers_for_min = {2, 4}
        game = NumericalTicTacToe(dimension=2)

        possible_numbers_for_max = game.possible_numbers(Max)
        possible_numbers_for_min = game.possible_numbers(Min)

        self.assertEqual(expected_possible_numbers_for_max, possible_numbers_for_max)
        self.assertEqual(expected_possible_numbers_for_min, possible_numbers_for_min)

    def test_get_possible_numbers_for_dimension_three(self):
        expected_possible_numbers_for_max = {1, 3, 5, 7, 9}
        expected_possible_numbers_for_min = {2, 4, 6, 8}
        game = NumericalTicTacToe(dimension=3)

        possible_numbers_for_max = game.possible_numbers(Max)
        possible_numbers_for_min = game.possible_numbers(Min)

        self.assertEqual(expected_possible_numbers_for_max, possible_numbers_for_max)
        self.assertEqual(expected_possible_numbers_for_min, possible_numbers_for_min)

    def test_get_possible_numbers_for_dimension_four(self):
        expected_possible_numbers_for_max = {1, 3, 5, 7, 9, 11, 13, 15}
        expected_possible_numbers_for_min = {2, 4, 6, 8, 10, 12, 14, 16}
        game = NumericalTicTacToe(dimension=4)

        possible_numbers_for_max = game.possible_numbers(Max)
        possible_numbers_for_min = game.possible_numbers(Min)

        self.assertEqual(expected_possible_numbers_for_max, possible_numbers_for_max)
        self.assertEqual(expected_possible_numbers_for_min, possible_numbers_for_min)

    def test_available_numbers(self):
        expected_available_numbers = [3]

        board = get_nearly_complete_board()
        state = GameState(board, Max)
        game = NumericalTicTacToe()

        self.assertEqual(expected_available_numbers, game.available_numbers(state))

    def test_winning_sum_for_dimension_two(self):
        expected_winning_sum = 5
        game = NumericalTicTacToe(dimension=2)
        self.assertEqual(expected_winning_sum, game.winning_sum)

    def test_winning_sum_for_dimension_three(self):
        expected_winning_sum = 15
        game = NumericalTicTacToe(dimension=3)
        self.assertEqual(expected_winning_sum, game.winning_sum)

    def test_winning_sum_for_dimension_four(self):
        expected_winning_sum = 34
        game = NumericalTicTacToe(dimension=4)
        self.assertEqual(expected_winning_sum, game.winning_sum)

    def test_get_all_possible_wins(self):
        game = NumericalTicTacToe(dimension=4)

        all_possible_wins = game.get_all_possible_wins()

        self.assertEqual(len(all_possible_wins), 86)

        self.assertIn({1, 15, 2, 16}, all_possible_wins)
        self.assertIn({1, 4, 14, 15}, all_possible_wins)
        self.assertIn({1, 7, 10, 16}, all_possible_wins)
        self.assertIn({2, 6, 11, 15}, all_possible_wins)
        self.assertIn({4, 5, 12, 13}, all_possible_wins)
        self.assertIn({3, 8, 9, 14}, all_possible_wins)

    def test_evaluate(self):
        board = {(0, 0): 2, (0, 1): 0, (0, 2): 0, (0, 3): 0,
                 (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0,
                 (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
                 (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0}
        player = Max
        state = GameState(board, player)
        game = NumericalTicTacToe(dimension=4)
        result = game.evaluate(state)
        self.assertEqual(result, 24)


def get_nearly_complete_board():
    return {(0, 0): 10, (0, 1): 16, (0, 2): 12, (0, 3): 6,
            (1, 0): 0, (1, 1): 13, (1, 2): 11, (1, 3): 14,
            (2, 0): 1, (2, 1): 9, (2, 2): 15, (2, 3): 0,
            (3, 0): 5, (3, 1): 4, (3, 2): 7, (3, 3): 8}


if __name__ == '__main__':
    unittest.main()
