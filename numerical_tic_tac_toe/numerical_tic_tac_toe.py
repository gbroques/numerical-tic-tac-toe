from itertools import product

from adversarial_search import Game
from .action import Action
from .game_state import GameState
from .player import Max
from .player import Min


class NumericalTicTacToe(Game):
    def __init__(self, dimension=4, winning_sum=34):
        self.dimension = dimension
        self.winning_sum = winning_sum
        initial_state = self.get_initial_state()
        super().__init__(initial_state)

    def get_initial_state(self):
        board = self.get_initial_board()
        initial_player = Max
        return GameState(board, initial_player)

    def get_initial_board(self):
        coordinates = self.get_board_coordinates()
        return {coordinate: 0 for coordinate in coordinates}

    def get_board_coordinates(self):
        """Get a list of tuples representing board coordinates.

        [(0, 0), (0, 1), (0, 2), ..., (3, 1), (3, 2), (3, 3)]
        """
        return list(product(range(self.dimension), repeat=2))

    def player(self, state):
        return state.player

    def actions(self, state):
        return [Action(c, n) for c in state.empty_spots for n in state.available_numbers]

    def possible_actions(self, player):
        """Return a player's possible actions.

        Possibles actions are a list of tuples in the form of ((x,  y), number),
        where (x, y) is a board position, and number is the numerical move.
        :param player:
        :return: List of possible actions.
        """
        coordinates = self.get_board_coordinates()
        return [Action(c, v) for v in player.possible_numbers() for c in coordinates]

    def result(self, state, action):
        if action.coordinate not in state.empty_spots:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[action.coordinate] = action.number
        next_player = Max if state.player.is_min() else Min
        return GameState(board, next_player)

    def terminal_test(self, state):
        prev_player = Max if state.player.is_min() else Max
        return self.utility(state, prev_player) != 0 or state.is_board_empty()

    def utility(self, state, player):
        if self.is_win(state.board):
            return +1 if player == Max else -1
        else:
            return 0

    def is_win(self, board):
        matrix = self.get_matrix_from_board(board)

        win_tests = [self.is_horizontal_win,
                     self.is_vertical_win,
                     self.is_diagonal_win]

        for win_test in win_tests:
            if win_test(matrix, self.winning_sum):
                return True

        return False

    def get_matrix_from_board(self, board):
        """Get two-dimensional matrix."""
        numbers = list(board.values())
        return [numbers[i: i + self.dimension] for i in range(0, len(numbers), self.dimension)]

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
