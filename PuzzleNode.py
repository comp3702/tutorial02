# State representation
from __future__ import annotations

from typing import List, Tuple, Optional

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

actions = {
    LEFT: 'L',
    RIGHT: 'R',
    UP: 'U',
    DOWN: 'D'
}

costs = {
    UP: 1,
    DOWN: 2,
    LEFT: 3,
    RIGHT: 4
}
costs.setdefault(0)

class PuzzleNode:

    def __init__(self, parent: Optional[PuzzleNode], action: Optional[int], current_state: Tuple[Tuple[int, ...], ...]):
        self.parent = parent
        self.action = action
        self.current_state = current_state

        self.blank_row, self.blank_col = self.find_blank()
        self.last_col = len(current_state) - 1
        self.last_row = len(current_state[0]) - 1

        self.cost = costs.get(action, 0)

    def find_blank(self) -> Tuple[int, int]:
        for row_index, row in enumerate(self.current_state):
            if -1 in row:
                return row_index, row.index(-1)

    def actions(self) -> List[int]:
        actions = list[int]()

        if self.blank_col > 0:
            actions.append(LEFT)
        if self.blank_col < self.last_col:
            actions.append(RIGHT)
        if self.blank_row > 0:
            actions.append(UP)
        if self.blank_row < self.last_row:
            actions.append(DOWN)

        return actions

    def step(self, action: int) -> Tuple[Tuple[int]]:
        new_state = list(list(row) for row in self.current_state)

        if self.blank_row == 0 and action == UP \
            or self.blank_row == self.last_row and action == DOWN \
            or self.blank_col == 0 and action == LEFT \
            or self.blank_col == self.last_col and action == RIGHT:
            raise Exception('Fell off the grid!')

        if action == UP:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row - 1][self.blank_col]
            new_state[self.blank_row - 1][self.blank_col] = -1
        elif action == DOWN:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row + 1][self.blank_col]
            new_state[self.blank_row + 1][self.blank_col] = -1
        elif action == LEFT:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col - 1]
            new_state[self.blank_row][self.blank_col - 1] = -1
        elif action == RIGHT:
            new_state[self.blank_row][self.blank_col] = new_state[self.blank_row][self.blank_col + 1]
            new_state[self.blank_row][self.blank_col + 1] = -1

        return tuple([tuple(row) for row in new_state])

    def print(self):
        print(f'Action taken: {actions[self.action]}' )
        for row in self.current_state:
            print(' '.join([str(item) for item in row]))
        print("\n\n")

    def __lt__(self, other: PuzzleNode):
        return self.cost < other.cost
