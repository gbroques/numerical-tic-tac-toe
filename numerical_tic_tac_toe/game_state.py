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

    @property
    def available_numbers(self):
        possible_numbers = self.player.possible_numbers()
        return list(filter(lambda n: n not in self.board.values(), possible_numbers))

    def __eq__(self, other):
        return (self.board == other.board and
                self.player == self.player)
