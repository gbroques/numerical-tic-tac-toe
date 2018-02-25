import unittest

from numerical_tic_tac_toe import NumericalTicTacToe
from numerical_tic_tac_toe import State


class TestNumericalTicTacToe(unittest.TestCase):

    def test_initial_state(self):
        expected_initial_state = State([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        game = NumericalTicTacToe()
        self.assertEqual(expected_initial_state, game.get_initial_state())


if __name__ == '__main__':
    unittest.main()
