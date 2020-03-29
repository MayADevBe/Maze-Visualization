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


class RecusiveDevision:

    def __init__(self, field):
        self.field = field

    def recusive_step(self, x1, x2, y1, y2):

        if x1+2 > x2 or y1+2 > y2:
            return

        #divide by two walls (even)
        xr = random.randint(x1+1, x2-1)
        yr = random.randint(y1+1, y2-1)
        if not xr%2==0:
            if not xr+1 >= x2:
                xr = xr+1
            elif not xr-1 <= x1:
                xr = xr-1
            else:
                return #TODO
        if not yr%2==0:
            if not yr+1 >= y2:
                yr = yr+1
            elif not yr-1 <= y1:
                yr = yr-1
            else:
                return #TODO
        for i in range(y1, y2+1):
            self.field[xr][i] = 0
        for j in range(x1, x2+1):
            self.field[j][yr] = 0
        #holes in wall (odd)
        try:
            xp1 = random.randint(x1+1, xr-1)
        except:
            xp1 = x1+1
        try:
            xp2 = random.randint(xr+1, x2-1)
        except:
            xp2 = xr+1
        if not xp1%2==1:
            if not xp1+1 >= xr:
                xp1 = xp1+1
            elif not xp1-1 <= x1:
                xp1 = xp1-1
            else:
                xp1 = xr-1
        if not xp2%2==1:
            if not xp2+1 >= x2:
                xp2 = xp2+1
            elif not xp2-1 <= xr:
                xp2 = xp2-1
            else:
                xp2 = xr+1
        yp = random.randint(y1+1, y2-1)
        if not yp%2==1:
            if not yp+1 >= y2:
                yp = yp+1
            elif not yp-1 <= y1:
                yp = yp-1
            else:
                yp = yp+1
        self.field[xr][yp] = 1
        self.field[xp1][yr] = 1
        self.field[xp2][yr] = 1
        #recursion
        self.recusive_step(x1, xr-1, y1, yr-1)
        self.recusive_step(xr+1, x2, y1, yr-1)
        self.recusive_step(x1, xr-1, yr+1, y2)
        self.recusive_step(xr+1, x2, yr+1, y2)

    def start_recursive(self):
        #original chamber
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if i == 0 or i == len(self.field)-1 or j == 0 or j == len(self.field)-1:
                    self.field[i][j] = 0
                else:
                    self.field[i][j] = 1
        #start recursion
        self.recusive_step(1, len(self.field)-2, 1, len(self.field)-2)