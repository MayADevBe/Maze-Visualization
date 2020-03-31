from board import Board
from math import floor
from generation import Prim, RecusiveDevision
from solve import Backtracking

def set_start_goal(event):
    global start, goal, board
    item = board.platform.find_closest(event.x, event.y)[0]
    x = floor(event.x/W_H)
    y = floor(event.y/W_H)
    if not board.field[x][y] == 0:
        if start == None:
            start = (x, y)
            board.platform.itemconfig(item, fill='blue')
        elif start == (x, y):
            start = None
            board.platform.itemconfig(item, fill='white')
        elif goal == None:
            goal = (x,y)
            board.field[x][y] = 2
            board.platform.itemconfig(item, fill='blue')
        elif goal == (x,y):
            goal = None
            board.field[x][x] = 1
            board.platform.itemconfig(item, fill='white')
        board.platform.update()

def start_solve(event=None):
    global solved
    if not start == None and not goal == None and generated and solved == None:
        solve = Backtracking(board, start[0], start[1])
        solved = solve.solve()
        if solved:
            color ="green"
        else:
            color = "red"
        board.color(color)
        board.platform.update()

def prim_generation(event=None):
    global generated
    prim_generation = Prim(board)
    prim_generation.prim_generate()
    generated = True
    board.draw()
    board.platform.update()

def recursive_devision_generation(event=None):
    global generated
    rec_generation = RecusiveDevision(board)
    rec_generation.start_recursive()
    generated = True
    board.draw()
    board.platform.update()

def reset(event=None):
    global start, goal, generated, solved
    start = None
    goal = None
    generated = False
    solved = None
    board.field = []
    board.draw()
    board.platform.update()

if __name__ == '__main__':
    R_C = 21
    W_H = 30
    start = None
    goal = None
    generated = False
    solved = None
    board = Board("Maze", W_H, R_C)
    board.platform.bind("<Button-1>", set_start_goal)
    board.platform.bind("<Return>", start_solve)
    board.platform.bind("<space>", reset)
    board.platform.bind("<p>", prim_generation)
    board.platform.bind("<r>", recursive_devision_generation)
    board.platform.focus_set()
    board.draw()
    board.start()
