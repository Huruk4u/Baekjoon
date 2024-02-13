import sys


def check_row(row):
    global board, num
    sub_col = num - set(board[row])
    return sub_col


def check_col(col, a):
    global board
    for i in range(9):
        if board[i][col] == a:
            return False
    return True


def check_3by3(row, col, a):
    global board

    mx = (col // 3) * 3
    my = (row // 3) * 3
    for i in range(my, my + 3):
        for j in range(mx, mx + 3):
            if board[i][j] == a:
                return False
    return True


def backtracking(idx):
    global board, blank
    # exit point
    if idx == len(blank):
        for _ in range(9):
            print(*board[_])
        exit(0)
    x = blank[idx][1]
    y = blank[idx][0]
    sub_row = check_row(y)
    for n in sub_row:
        if check_col(x, n) and check_3by3(y, x, n):
            board[y][x] = n
            backtracking(idx+1)
            board[y][x] = 0


if __name__ == '__main__':
    # input
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
    num = set([i for i in range(1, 10)])

    blank = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.append([i, j])

    backtracking(0)
