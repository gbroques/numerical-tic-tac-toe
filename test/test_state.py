import unittest

from numerical_tic_tac_toe import State


class TestState(unittest.TestCase):
    def test_equals(self):
        a = State([[1, 2], [3, 4], [5, 6]])
        b = State([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
