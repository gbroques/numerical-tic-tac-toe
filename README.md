# Numerical Tic-tac-toe

[![Build Status](https://travis-ci.org/gbroques/numerical-tic-tac-toe.svg?branch=master)](https://travis-ci.org/gbroques/numerical-tic-tac-toe)

A numerical tic-tac-toe player written in Python 3 with a 4 x 4 board.

![Numerical Tic-tac-toe board](4x4-numerical-tic-tac-toe.svg)

Numerical tic-tac-toe is similar to normal tic-tac-toe, except instead of X's and O's, the two players are given the numbers:

* {1, 3, 5, 7, 9, 11, 13, 15}
* {2, 4, 6, 8, 10, 12, 14, 16}

Respectively.

The players take turns (the odd player goes first) and each round a player puts one unused number on an open spot on the board. The goal is to have 4 numbers in a line sum to 34 (the average of te numbers 1 - 16).

There's two ways to play:

1. The computer against a human player, with the player choosing to go first or second.

2. The computer plays itself, talking alternating moves, allowing a human to watch by pressing a key to continue for each successive move.

## Evaluation Function
Currently the evaluation function separates the board into 10 vectors, scoring each vector individually, and summing each score.

How does it score each board vector?
First it computes all possible winning vectors, and checks if it is a subset of a winning vector.
If it's not, then the vector gets 0 points.
If it is a subset of a winning vector, then the number of even and odd numbers in the vector is computed.
The worst scenario for Max, 4 even, is given -32 points.
While the best scenario for Max, 2 odd and 2 even, or 4 odd, is given 32 points.
Other scenarios are given an appropriate score on a power of 2 scale.
See the below evaluation function.

```python
def evaluate(self, state):
    all_possible_wins = get_all_possible_wins()
    vectors = get_board_vectors(state)
    score = 0
    for v in vectors:
        if not self.is_subset(v, all_possible_wins):
            continue
        num_even = len([e for e in v if e % 2 == 0 and e != 0])
        num_odd = len([e for e in v if e % 2 == 1])
        if (num_odd == 2 and num_even == 2) or (num_odd == 4 and num_even == 0):
            score += 32
        if num_odd == 0 and num_even == 4:
            score -= 32
        elif num_odd == 1 and num_even == 2:
            score += 16
        elif num_odd == 0 and num_even == 1:
            score += 8
        elif num_odd == 1 and num_even == 0:
            score += 4
        elif num_odd == 1 and num_even == 1:
            score += 2
        elif num_odd == 2 and num_even == 1:
            score += 1
    return score
```

## References

***Artificial Intelligence: A Modern Approach* (AIMA)** (3rd Edition) by Stuart J. Russel and Peter Norvig

Section 5.2 Optimal Decisions in Games

https://github.com/aimacode/aima-python/blob/master/games.py
