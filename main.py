from board import Board
from generation import Prim, RecusiveDevision

if __name__ == '__main__':
    R_C = 21
    W_H = 30
    board = Board("Maze", W_H, R_C)
    board.draw()
    # prim_generation = Prim(board.field)
    # prim_generation.prim_generate()
    rec_generation = RecusiveDevision(board.field)
    rec_generation.start_recursive()
    board.draw()
    board.start()