from itertools import product
from math import pow
from random import randint
from sys import exit

from adversarial_search import AlphaBetaCutoff
from adversarial_search import Game
from .action import Action
from .game_mode import GameMode
from .game_state import GameState
from .player import Max
from .player import Min


class NumericalTicTacToe(Game):
    def __init__(self, dimension=4):
        self.dimension = dimension
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

    def play(self):
        state = self.initial_state
        print(state)
        game_mode = self._get_game_mode()
        if game_mode.is_human_vs_computer():
            self._init_human_vs_computer_loop(state)
        else:
            self._init_computer_vs_computer_loop(state)

    @staticmethod
    def _get_game_mode():
        human_vs_computer = ''
        while human_vs_computer.lower() != 'y' and human_vs_computer.lower() != 'n':
            human_vs_computer = input('Would you like to play? (Y/n) ')
            if human_vs_computer == '':
                human_vs_computer = 'y'
        return GameMode.HUMAN_VS_COMPUTER if human_vs_computer.lower() == 'y' else GameMode.COMPUTER_VS_COMPUTER

    def _init_human_vs_computer_loop(self, state):
        human_player = self.get_human_player()
        while True:
            for player in self.players():
                if player == human_player:
                    action = self._get_user_action(state)
                else:
                    action = AlphaBetaCutoff.search(state, self, eval_fn=self.evaluate)
                state = self.result(state, action)
                print(state)
                if self.terminal_test(state):
                    print("Game over!")
                    exit(0)

    def _init_computer_vs_computer_loop(self, state):
        while True:
            enter = '-1'
            while enter != '':
                enter = input('Press Enter to continue.')
            action = AlphaBetaCutoff.search(state, self, eval_fn=self.evaluate)
            state = self.result(state, action)
            print(state)
            if self.terminal_test(state):
                print("Game over!")
                exit(0)

    @staticmethod
    def get_human_player():
        go_first = ''
        while go_first.lower() != 'y' and go_first.lower() != 'n':
            go_first = input('Would you like to go first? (Y/n) ')
            if go_first == '':
                go_first = 'y'
        return Max if go_first.lower() == 'y' else Min

    @staticmethod
    def evaluate(state):
        return randint(0, 9)

    def _get_user_action(self, state):
        coordinate = self._get_coordinate(state)
        number = self._get_number(state)
        action = Action(coordinate, number)
        return action

    def _get_coordinate(self, state):
        position = -1
        positions = [self._map_coordinate_to_position(c) for c in state.empty_spots]
        while position not in positions:
            try:
                position = int(input(self._get_position_prompt(positions)))
            except ValueError:
                pass
        return self._map_position_to_coordinate(position)

    @classmethod
    def _get_position_prompt(cls, positions):
        return cls._get_prompt('position', positions)

    @staticmethod
    def _get_prompt(prompt_for, possible_options):
        options = ', '.join(str(o) for o in possible_options)
        return 'Enter a ' + prompt_for + ' (' + options + '): '

    def _map_position_to_coordinate(self, position):
        coordinates = self.get_board_coordinates()
        return coordinates[position]

    def _map_coordinate_to_position(self, coordinate):
        coordinates = self.get_board_coordinates()
        return coordinates.index(coordinate)

    def _get_number(self, state):
        number = -1
        available_numbers = self.available_numbers(state)
        while number not in available_numbers:
            try:
                number = int(input(self._get_number_prompt(available_numbers)))
            except ValueError:
                pass
        return number

    @classmethod
    def _get_number_prompt(cls, available_numbers):
        return cls._get_prompt('number', available_numbers)

    def player(self, state):
        return state.player

    @staticmethod
    def players():
        return [Max, Min]

    def actions(self, state):
        return [Action(c, n) for c in state.empty_spots for n in self.available_numbers(state)]

    def available_numbers(self, state):
        possible_numbers = self.possible_numbers(state.player)
        return list(filter(lambda n: n not in state.board.values(), possible_numbers))

    def possible_actions(self, player):
        """Return a player's possible actions.

        Possibles actions are a list of tuples in the form of ((x,  y), number),
        where (x, y) is a board position, and number is the numerical move.
        :param player:
        :return: List of possible actions.
        """
        coordinates = self.get_board_coordinates()
        return [Action(c, v) for v in self.possible_numbers(player) for c in coordinates]

    def possible_numbers(self, player):
        start = 1 if player.is_max() else 2
        num_tiles = int(pow(self.dimension, 2))
        return set(range(start, num_tiles + 1, 2))

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
            return +1 if player.is_max() else -1
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

    def is_horizontal_win(self, matrix, winning_sum):
        count = 0
        in_a_row = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    count += matrix[i][j]
                    in_a_row += 1
                if count == winning_sum and in_a_row == self.dimension:
                    return True
            count = 0
            in_a_row = 0
        return False

    def is_vertical_win(self, matrix, winning_sum):
        transpose = list(zip(*matrix))
        return self.is_horizontal_win(transpose, winning_sum)

    def is_diagonal_win(self, matrix, winning_sum):
        is_major_win = self.is_major_diagonal_win(matrix, winning_sum)
        is_minor_win = self.is_minor_diagonal_win(matrix, winning_sum)
        return is_major_win or is_minor_win

    @staticmethod
    def is_major_diagonal_win(matrix, winning_sum):
        major_diagonal = [matrix[i][i] for i in range(0, len(matrix))]
        is_major_non_zero = all(major_diagonal)
        return sum(major_diagonal) == winning_sum and is_major_non_zero

    @staticmethod
    def is_minor_diagonal_win(matrix, winning_sum):
        minor_diagonal = [matrix[i][~i] for i in range(0, len(matrix))]
        is_minor_non_zero = all(minor_diagonal)
        return sum(minor_diagonal) == winning_sum and is_minor_non_zero

    @property
    def winning_sum(self):
        d = self.dimension
        return d * (d ** 2 + 1) / 2
