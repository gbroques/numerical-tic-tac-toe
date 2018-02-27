import unittest

from numerical_tic_tac_toe import GameState
from numerical_tic_tac_toe import Max
from test.test_numerical_tic_tac_toe import get_nearly_complete_board


class TestGameState(unittest.TestCase):
    def test_empty_spots(self):
        expected_empty_spots = [(1, 0), (2, 3)]

        board = get_nearly_complete_board()
        state = GameState(board, Max)

        self.assertEqual(expected_empty_spots, state.empty_spots)


if __name__ == '__main__':
    unittest.main()
