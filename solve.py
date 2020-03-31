from copy import deepcopy
import time

class Backtracking:

    def __init__(self, board, start_x, start_y):
        self.board = board
        self.field = board.field
        self.start_x = start_x
        self.start_y = start_y

    def solve(self):
        return self.recursive_step(self.start_x, self.start_y)

    def recursive_step(self, x, y):
        self.board.color("orange")
        self.board.platform.update()
        time.sleep(0.1)
        if self.field[x][y] == 2: #goal
            return True
        elif self.field[x][y] == 1: #not explored
            self.field[x][y] = 3
            #recursion
            if x < len(self.field)-1:
                if self.recursive_step(x+1, y):
                    return True
            if x > 0:
                if self.recursive_step(x-1, y):
                    return True
            if y < len(self.field[0])-1:
                if self.recursive_step(x, y+1):
                    return True
            if y > 0:
                if self.recursive_step(x, y-1):
                    return True
            self.field[x][y] = 4