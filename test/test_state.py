import unittest

from numerical_tic_tac_toe import GameState
from numerical_tic_tac_toe import Max


class TestGameState(unittest.TestCase):
    def test_equals(self):
        a = GameState([[1, 2], [3, 4]], Max)
        b = GameState([[1, 2], [3, 4]], Max)
        self.assertEqual(a, b)

    def test_current_player(self):
        a = GameState([1], Max)
        self.assertEqual(a.player, Max)


if __name__ == '__main__':
    unittest.main()
