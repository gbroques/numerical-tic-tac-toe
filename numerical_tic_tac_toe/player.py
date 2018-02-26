from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self.name = name

    @staticmethod
    @abstractmethod
    def is_max():
        """Return True if player is Max."""

    @staticmethod
    @abstractmethod
    def is_min():
        """Return True if player is Min."""

    @staticmethod
    @abstractmethod
    def possible_numbers():
        """Return a set of possible numbers for moves."""

    def __str__(self):
        return '<{}>'.format(self.name)

    def __repr__(self):
        return '<{}>'.format(self.name)


class Max(Player):
    def __init__(self):
        super(Max, self).__init__(self.__class__.__name__)

    @staticmethod
    def is_max():
        return True

    @staticmethod
    def is_min():
        return False

    @staticmethod
    def possible_numbers():
        return {1, 3, 5, 7, 9, 11, 13, 15}


class Min(Player):
    def __init__(self):
        super(Min, self).__init__(self.__class__.__name__)

    @staticmethod
    def is_max():
        return False

    @staticmethod
    def is_min():
        return True

    @staticmethod
    def possible_numbers():
        return {2, 4, 6, 8, 10, 12, 14, 16}
