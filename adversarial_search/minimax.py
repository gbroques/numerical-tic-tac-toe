"""
Depth-limited minimax

Sources:
https://github.com/aimacode/aima-python/blob/master/search.py
https://github.com/aimacode/aima-python/blob/master/games.py
"""

from random import randint

infinity = float('inf')


def minimax_decision(state, game, limit=2):
    """Given a state in a game, calculate the best move by searching
    forward all the way to the terminal state."""

    return max(game.actions(state),
               key=lambda a: min_value(game.result(state, a), game, limit))


def max_value(state, game, limit):
    if game.terminal_test(state):
        return game.utility(state, state.player)
    elif limit == 0:
        minimax_value = max([evaluate(game.result(state, a)) for a in game.actions(state)])
        return minimax_value
    else:
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a), game, limit - 1))
        return v


def min_value(state, game, limit):
    if game.terminal_test(state):
        return game.utility(state, state.player)
    elif limit == 0:
        minimax_value = min([evaluate(game.result(state, a)) for a in game.actions(state)])
        return minimax_value
    else:
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a), game, limit - 1))
        return v


def evaluate(state):
    return randint(0, 9)
