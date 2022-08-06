# Tutorial 02
## Breadth First Search, Depth First Search and Uniform Cost Search

Loosely based on [Tutorial_2_solution.py](official/Tutorial_2_solutions.py.txt).

The original solutions are in [official](official) folder.

The main differences to the other solutions:

1) It uses agent taking actions/steps in environment paradigm - rather than graph / node / children paradigm (similar to Nick's solution)
2) Hides the Node implementation from the end user by accepting 2D arrays as initial and goal state
3) Keeps the state as immutable tuple of tuples rather than lists
4) Fixes naming conventions and caches some calculations to make the code more readable
5) __There are unit tests__ - for the PuzzleNode as well as the searches - I am hoping they will help with debugging issues faced by the students
6) It's faster and uses less memory than the other solutions - __although it is still not good enough to solve the 15-puzzle__ - see the [main.py](main.py)