from abc import ABC, abstractmethod


class Game(ABC):
    """Abstract class to represent games as a adversarial search problem.

    Reference:
    Artificial Intelligence: A Modern Approach (3rd edition) by Stuart J. Russel and Peter Norvig
    Page 162
    """

    def __init__(self, initial_state):
        self.initial_state = initial_state

    @abstractmethod
    def player(self, state):
        """Defines which player has the move in a state."""

    @abstractmethod
    def actions(self, state):
        """Returns the set of legal moves in a state."""

    @abstractmethod
    def result(self, state, action):
        """The transition model, which defines the result of the move."""

    @abstractmethod
    def terminal_test(self, state):
        """Returns True when the game is over and False otherwise.

        States where the game has ended are called terminal states.
        """

    @abstractmethod
    def utility(self, state, player):
        """Defines the numerical value for a game that ends in the given state for the given player."""
