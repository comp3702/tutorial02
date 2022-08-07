import heapq
import unittest

from PuzzleNode import PuzzleNode, UP, DOWN, LEFT, RIGHT
from uniform_cost_search import uniform_cost_search


class TestUniformCostSearch(unittest.TestCase):
    def test_heapq(self):
        cost1 = PuzzleNode(None, UP, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost2 = PuzzleNode(None, DOWN, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost3 = PuzzleNode(None, LEFT, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))
        cost4 = PuzzleNode(None, RIGHT, ((1, 2, 3), (4, 5, 6), (7, 8, -1)))

        heap = [cost4, cost2, cost3, cost1]
        heapq.heapify(heap)

        self.assertEqual([cost1, cost2, cost3, cost4], list(heap))

    def test_one_step(self):
        start = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        goal = (
            (1, 2, 3),
            (4, 5, -1),
            (7, 8, 6)
        )

        steps = uniform_cost_search(start, goal)
        self.assertEqual(2, len(steps) )

    def test_hard(self):
        init_state = (
            (7, 2, 4),
            (5, 3, 6),
            (8, -1, 1)
        )
        goal_state = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, -1)
        )
        steps = uniform_cost_search(init_state, goal_state)
        self.assertEqual(20, len(steps))
