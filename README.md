# Numerical Tic-tac-toe

[![Build Status](https://travis-ci.org/gbroques/numerical-tic-tac-toe.svg?branch=master)](https://travis-ci.org/gbroques/numerical-tic-tac-toe)

A numerical tic-tac-toe player written in Python 3 with a 4 x 4 board.

Numerical tic-tac-toe is similar to normal tic-tac-toe, except instead of X's and O's, the two players are given the numbers:

* {1, 3, 5, 7, 9, 11, 13, 15}
* {2, 4, 6, 8, 10, 12, 14, 16}

Respectively.

The players take turns (the odd player goes first) and each round a player puts one unused number on an open spot on the board. The goal is to have 4 numbers in a line sum to 34 (the average of te numbers 1 - 16).

There's two ways to play:

1. The computer against a human player, with the player choosing to go first or second.

2. The computer plays itself, talking alternating moves, allowing a human to watch by pressing a key to continue for each successive move.


## References

***Artificial Intelligence: A Modern Approach* (AIMA)** (3rd Edition) by Stuart J. Russel and Peter Norvig

Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
