import unittest

from adversarial_search import Max
from numerical_tic_tac_toe import GameState


class TestGameState(unittest.TestCase):
    def test_equals(self):
        a = GameState([[1, 2], [3, 4]], Max)
        b = GameState([[1, 2], [3, 4]], Max)
        self.assertEqual(a, b)

    def test_current_player(self):
        a = GameState([1], Max)
        self.assertEqual(a.current_player, Max)


if __name__ == '__main__':
    unittest.main()
