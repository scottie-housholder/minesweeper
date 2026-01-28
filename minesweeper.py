import random

def make_board(size):
    # print(list([list([0]*size)]*size)) #I think this version is slower
    return [[0 for _ in range(size)] for _ in range(size)]


def fill_board(board, num_mines):
    pass


def main():
    board = make_board(8)
    fill_board(board)



main()