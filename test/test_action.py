import unittest

from numerical_tic_tac_toe import Action


class TestAction(unittest.TestCase):
    def test_equals(self):
        a = Action((0, 0), 1)
        b = Action((0, 0), 1)

        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
