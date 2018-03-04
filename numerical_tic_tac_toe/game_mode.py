from enum import Enum, auto


class GameMode(Enum):
    HUMAN_VS_COMPUTER = auto()
    COMPUTER_VS_COMPUTER = auto()

    def is_human_vs_computer(self):
        return self is GameMode.HUMAN_VS_COMPUTER

    def is_computer_vs_computer(self):
        return self is GameMode.COMPUTER_VS_COMPUTER
