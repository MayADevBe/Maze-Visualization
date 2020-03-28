import random

class Prim:

    def __init__(self, field):
        self.field = field
        self.frontier = []

    def add_frontier(self, x, y):
        if x > 2 and (not (x-2, y) in self.frontier) and self.field[x-2][y] == 0:
            self.frontier.append((x-2, y))
        if y > 2 and (not (x, y-2) in self.frontier) and self.field[x][y-2] == 0:
            self.frontier.append((x, y-2))
        if x < (len(self.field)-3) and (not (x+2, y) in self.frontier) and self.field[x+2][y] == 0:
            self.frontier.append((x+2, y))
        if y < (len(self.field)-3) and (not (x, y+2) in self.frontier) and self.field[x][y+2] == 0:
            self.frontier.append((x, y+2))

    def get_neighbour(self, x, y):
        neighbour = []
        if x > 2 and self.field[x-2][y] == 1:
            neighbour.append((x-2, y))
        if y > 2 and self.field[x][y-2] == 1:
            neighbour.append((x, y-2))
        if x < (len(self.field)-3)  and self.field[x+2][y] == 1:
            neighbour.append((x+2, y))
        if y < (len(self.field)-3) and self.field[x][y+2] == 1:
            neighbour.append((x, y+2))

        if len(neighbour) > 0 :
            r = random.randint(0, len(neighbour)-1)
            i, j = neighbour[r]

            if x > i:
                return (i+1, j)
            elif x < i:
                return (i-1, j)
            elif y > j:
                return (i, j+1)
            elif y < j:
                return (i, j-1)
            else:
                print("No Neighbour")
                return (i, j)
        return (0, 0)

    def prim_generate(self):
        #pick random cell (ignoring outer walls)
        x = random.randint(1, len(self.field)-2)
        y = random.randint(1, len(self.field)-2)
        self.field[x][y] = 1 # passage
        self.add_frontier(x, y)

        while not len(self.frontier) == 0:
            i = random.randint(0, len(self.frontier)-1)
            x, y = self.frontier[i]
            a, b = self.get_neighbour(x, y)
            if not a == 0 and not b == 0:    
                self.field[a][b] = 1
            self.add_frontier(x, y)
            self.field[x][y] = 1
            self.frontier.pop(i)