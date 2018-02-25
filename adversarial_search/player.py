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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Max(Player):
    def __init__(self):
        super(Max, self).__init__(self.__class__.__name__)

    @staticmethod
    def is_max():
        return True

    @staticmethod
    def is_min():
        return False


class Min(Player):
    def __init__(self):
        super(Min, self).__init__(self.__class__.__name__)

    @staticmethod
    def is_max():
        return False

    @staticmethod
    def is_min():
        return True
