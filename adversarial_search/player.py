from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def is_max(self):
        """Return True if player is Max."""

    @abstractmethod
    def is_min(self):
        """Return True if player is Min."""

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Max(Player):
    def __init__(self):
        super(Max, self).__init__(self.__class__.__name__)

    def is_max(self):
        return True

    def is_min(self):
        return False


class Min(Player):
    def __init__(self):
        super(Min, self).__init__(self.__class__.__name__)

    def is_max(self):
        return False

    def is_min(self):
        return True
