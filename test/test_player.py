import unittest

from numerical_tic_tac_toe import Max
from numerical_tic_tac_toe import Min


class TestPlayer(unittest.TestCase):

    def test_possible_numbers_for_max(self):
        expected_possible_numbers_for_max = {1, 3, 5, 7, 9, 11, 13, 15}

        self.assertEqual(expected_possible_numbers_for_max, Max.possible_numbers())

    def test_possible_numbers_for_min(self):
        expected_possible_numbers_for_min = {2, 4, 6, 8, 10, 12, 14, 16}

        self.assertEqual(expected_possible_numbers_for_min, Min.possible_numbers())


if __name__ == '__main__':
    unittest.main()
