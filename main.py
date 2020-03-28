from board import Board
from generation import Prim

R_C = 21
W_H = 30
board = Board("Maze", W_H, R_C)
board.draw()
prim_generation = Prim(board.field)
prim_generation.prim_generate()
board.draw()
board.start()