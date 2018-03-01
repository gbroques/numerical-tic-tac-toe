"""
Depth-limited minimax

Sources:
https://github.com/aimacode/aima-python/blob/master/search.py
https://github.com/aimacode/aima-python/blob/master/games.py
"""

from random import randint
from threading import Timer

TIME_LIMIT = 60.0  # 1 minutes

infinity = float('inf')


class Minimax:
    _cutoff = False

    @classmethod
    def decision(cls, state, game, limit=50):
        """Given a state in a game, calculate the best move by searching
        forward all the way to the terminal state."""

        print("Deciding on move...")

        Timer(TIME_LIMIT, cls._set_cutoff).start()

        return max(game.actions(state),
                   key=lambda a: cls._min_value(game.result(state, a), game, limit))

    @classmethod
    def _max_value(cls, state, game, limit):
        if game.terminal_test(state):
            player = game.player(state)
            return game.utility(state, player)
        elif limit == 0 or cls._cutoff:
            minimax_value = max([cls._evaluate(game.result(state, a)) for a in game.actions(state)])
            return minimax_value
        else:
            v = -infinity
            for a in game.actions(state):
                v = max(v, cls._min_value(game.result(state, a), game, limit - 1))
            return v

    @classmethod
    def _min_value(cls, state, game, limit):
        if game.terminal_test(state):
            player = game.player(state)
            return game.utility(state, player)
        elif limit == 0 or cls._cutoff:
            minimax_value = min([cls._evaluate(game.result(state, a)) for a in game.actions(state)])
            return minimax_value
        else:
            v = infinity
            for a in game.actions(state):
                v = min(v, cls._max_value(game.result(state, a), game, limit - 1))
            return v

    @classmethod
    def _evaluate(cls, state):
        return randint(0, 9)

    @classmethod
    def _set_cutoff(cls):
        cls._cutoff = True
