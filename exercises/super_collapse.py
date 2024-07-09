from collections import deque


def color(integer):
    if integer == 1:
        integer = "r"
    elif integer == 2:
        integer = "b"
    elif integer == 3:
        integer = "y"
    elif integer == 4:
        integer = "w"
    elif integer == 0:
        ...
    else:
        raise ValueError(f"Invalid integer: {integer}")
    return integer

def adjecent_of(board, pos):
    (row, col) = pos

    color = board[row][col]

    height = len(board)
    width = len(board[0])

    if row + 1 < height and board[row + 1][col] == color:
        yield (row + 1, col)

    if row - 1 >= 0 and board[row - 1][col] == color:
        yield  (row - 1, col)

    if col + 1 < width and board[row][col + 1] == color:
        yield (row, col + 1)

    if col - 1 >= width and board[row][col - 1] == color:
        yield (row, col - 1)



def find_cluster(board, pos):
    (i, j) = pos

    que = deque()
    que.append(pos)
    return_values = []

    while len(que) != 0:
        item = que.popleft()
        if board[item[0]][item[1]] == board[i][j] and item not in return_values:
            return_values.append(item)

            for x in adjecent_of(board, item):
                que.append(x)

    if len(return_values) < 2:
        return []

    return return_values


def gravity(board):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for k in range(i - 1, -1, -1):
                    if board[k][j]!= 0:
                        board[i][j], board[k][j] = board[k][j], board[i][j]
                        break
    return board

def delete(board, position):
    cluster = find_cluster(board, position)

    for i in cluster:
        board[i[0]][i[1]] = 0

def show_board(board):
        
    row = len(board)
    for i in range(row):
        words_row = []
        words_row.append(f"{i} ")
        for j in range(len(board[0])):
            if j == len(board[i]) - 1:
                words_row.append(f"│{color(board[i][j])}│")
            else:
                words_row.append(f"│{color(board[i][j])}")
        print("  ", end="")
        print(f"{" _" * len(board[i])}")
        print(''.join(words_row))
    print("  ", end="")
    print(f"{" _" * len(board)}")
    print("   ", end="")
    for i in range(len(board[0])):
        print(f"{i} ", end="")




if __name__ == '__main__':
    board = [[0, 0, 0, 0, 2, 2, 2, 0, 0, 0], # height 10, width 10
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 0, 3, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 3, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 1, 0],
             [2, 2, 2, 0, 0, 0, 0, 4, 1, 4],
             [2, 1, 2, 3, 0, 0, 2, 4, 3, 2],
             [3, 1, 1, 4, 4, 3, 2, 4, 4, 3],
             [3, 3, 1, 4, 2, 3, 2, 2, 2, 1]]

    while True:
        board = gravity(board)
        show_board(board)
        delete(board, (int(input("\ny: ")), int(input("x: "))))



