class GameState:
    def __init__(self, board, current_player):
        """A class to represent the game's state.

        :param board: 4x4 dimensional list.
        :param current_player: The current player to make a move.
        """
        self.board = board
        self.current_player = current_player

    def __eq__(self, other):
        return self.board == other.board
