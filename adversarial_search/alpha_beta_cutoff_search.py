"""
Depth-limited minimax

Sources:
https://github.com/aimacode/aima-python/blob/master/search.py
https://github.com/aimacode/aima-python/blob/master/games.py
"""

from sys import maxsize
from threading import Timer

infinity = float('inf')


class AlphaBetaCutoff:
    _timeout = False

    @classmethod
    def search(cls, state, game, eval_fn=None, timeout_duration=2.0):
        timer = Timer(timeout_duration, cls._set_timeout)
        timer.start()
        minimax_value = None
        action = None
        for i in range(maxsize):
            try:
                minimax_value, action = cls._search(state, game, d=i, eval_fn=eval_fn)
            except TimeoutException:
                break
        timer.cancel()
        cls._timeout = False
        print("Minimax Value: " + str(minimax_value))
        return action

    @classmethod
    def _set_timeout(cls):
        cls._timeout = True

    @classmethod
    def _search(cls, state, game, d=4, cutoff_test=None, eval_fn=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""

        player = game.player(state)

        # Functions used by alpha beta
        def max_value(state, alpha, beta, depth):
            if cls._timeout:
                raise TimeoutException()
            elif cutoff_test(state, depth):
                return eval_fn(state)
            v = -infinity
            for a in game.actions(state):
                v = max(v, min_value(game.result(state, a),
                                     alpha, beta, depth + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(state, alpha, beta, depth):
            if cls._timeout:
                raise TimeoutException()
            elif cutoff_test(state, depth):
                return eval_fn(state)
            v = infinity
            for a in game.actions(state):
                v = min(v, max_value(game.result(state, a),
                                     alpha, beta, depth + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        # Body of alpha beta_cutoff_search starts here:
        # The default test cuts off at depth d or at a terminal state
        def is_cutoff(state, depth):
            return depth > d or game.terminal_test(state)

        cutoff_test = cutoff_test or is_cutoff

        eval_fn = eval_fn or (lambda state: game.utility(state, player))
        best_score = -infinity
        beta = infinity
        best_action = None
        for a in game.actions(state):
            v = min_value(game.result(state, a), best_score, beta, 1)
            if v > best_score:
                best_score = v
                best_action = a
        return best_score, best_action


class TimeoutException(Exception):
    pass
