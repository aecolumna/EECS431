board = [[0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

paths = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]



def validSquare(board, row, col):
    dimrow = len(board) - 1
    dimcol = len(board[0]) - 1

    if row > dimrow:
        return False

    if col > dimcol:
        return False

    if board[row][col] == 1:
        return False

    return True




def countPaths(board, row, col, paths):
    if not validSquare(board, row, col):
        return 0

    if row == 7 and col == 7:
        return 1

    if paths[row][col] == 0:
        paths[row][col] = countPaths(board, row + 1, col, paths) + countPaths(board, row, col + 1, paths)

    return paths[row][col]


countPaths(board, 0, 0, paths)

summation = 0
for i in range(8):
    for j in range(8):
        summation += paths[i][j]

print("sum : ",summation)

from pprint import pprint

pprint(paths)