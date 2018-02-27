from itertools import product

from adversarial_search import Game
from .action import Action
from .game_state import GameState
from .player import Max
from .player import Min

DIMENSION = 4


class NumericalTicTacToe(Game):
    def __init__(self):
        initial_state = self.get_initial_state()
        super().__init__(initial_state)

    @classmethod
    def get_initial_state(cls):
        board = cls.get_initial_board()
        initial_player = Max
        return GameState(board, initial_player)

    @classmethod
    def get_initial_board(cls):
        coordinates = cls.get_board_coordinates()
        return {coordinate: 0 for coordinate in coordinates}

    @staticmethod
    def get_board_coordinates():
        """Get a list of tuples representing board coordinates.

        [(0, 0), (0, 1), (0, 2), ..., (3, 1), (3, 2), (3, 3)]
        """
        return list(product(range(DIMENSION), repeat=2))

    def player(self, state):
        return state.player

    def actions(self, state):
        return [Action(c, n) for c in state.empty_spots for n in state.available_numbers]

    @classmethod
    def possible_actions(cls, player):
        """Return a player's possible actions.

        Possibles actions are a list of tuples in the form of ((x,  y), number),
        where (x, y) is a board position, and number is the numerical move.
        :param player:
        :return: List of possible actions.
        """
        coordinates = cls.get_board_coordinates()
        return [Action(c, v) for v in player.possible_numbers() for c in coordinates]

    def result(self, state, action):
        if action.coordinate not in state.empty_spots:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[action.coordinate] = action.number
        next_player = Max if state.player.is_min() else Min
        return GameState(board, next_player)

    def terminal_test(self, state):
        super().terminal_test(state)

    def utility(self, state, player):
        super().utility(state, player)

    @classmethod
    def is_won(cls, board):
        winning_sum = 34
        numbers = list(board.values())  # Get two-dimensional board
        matrix = [numbers[i: i + DIMENSION] for i in range(0, len(numbers), DIMENSION)]

        if cls.is_horizontal_win(matrix, winning_sum):
            return True

        if cls.is_vertical_win(matrix, winning_sum):
            return True

        if cls.is_diagonal_win(matrix, winning_sum):
            return True

        return False

    @staticmethod
    def is_horizontal_win(matrix, winning_sum):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                count += matrix[i][j]
                if count == winning_sum:
                    return True
            count = 0
        return False

    @classmethod
    def is_vertical_win(cls, matrix, winning_sum):
        transpose = list(zip(*matrix))
        return cls.is_horizontal_win(transpose, winning_sum)

    @staticmethod
    def is_diagonal_win(matrix, winning_sum):
        count = 0
        for i in range(len(matrix)):
            count += matrix[i][i]
            if count == winning_sum:
                return True
        return False
