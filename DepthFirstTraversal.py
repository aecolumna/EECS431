board = [[0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

dim = len(board[0])
visited = set()
stack = []


def search(start, end):
    if start == end:  # base case
        print(stack)
        return

    dim = len(board[0])
    nextRow = (start[0] + 1, start[1])
    nextCol = (start[0], start[1] + 1)

    row = start[0]
    col = start[1]

    if row < dim - 1 and board[row + 1][col] == 0:
        stack.append(start)
        search(nextRow, end)
        stack.pop()


    if col < dim - 1 :
        stack.append(start)
        search(nextCol, end)
        stack.pop()


search((0,0), (7,7))


