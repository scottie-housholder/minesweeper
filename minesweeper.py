import random

def print_board(board):
    for col in board:
        print(col)


def make_board(size):
    # print(list([list([0]*size)]*size)) #I think this version is slower
    board = [["E" for _ in range(size)] for _ in range(size)]
    return board


def fill_board(board, num_mines):
    # print(board)
    size = len(board)
    for _ in range(num_mines):
        row = random.randint(0, size-1)
        col = random.randint(0, size-1)
        board[row][col] = "M"


def main():
    board = make_board(8)
    fill_board(board, 10)
    print_board(board)



main()