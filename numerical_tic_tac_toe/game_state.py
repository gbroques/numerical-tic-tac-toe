from math import sqrt


class GameState:
    def __init__(self, board, player):
        """A class to represent the game's state.

        :param board: List of coordinates [(0, 0), ..., (3, 3)].
        :param player: The current player to make a move.
        """
        self.board = board
        self.player = player

    @property
    def empty_spots(self):
        return [k for k, v in self.board.items() if v == 0]

    def is_board_empty(self):
        return len(self.empty_spots) == 0

    def __eq__(self, other):
        return (self.board == other.board and
                self.player == self.player)

    def __str__(self):
        numbers = self.board.values()
        dimension = sqrt(len(numbers))
        string = ''
        for i, number in enumerate(numbers):
            if i % dimension == 0 and i != 0:
                string += '\n'
            string += ' ' + '{:>2}'.format(number) + ' '
        return string
