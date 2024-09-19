def solution(board):
    N = len(board)

    def in_range(y, x):
        if (0 <= x < N) and (0 <= y < N):
            return True
        else:
            return False

    def black_drop(y, x):
        for i in range(y):
            # x열의 y행 위에 뭔가 존재하면 검은 블록을 쌓을 수 없다.
            if board[i][x]:
                return False
        return True

    def crash(y, x, Y, X):
        if not in_range(y + Y - 1, x + X - 1): return False
        empty, value = 0, -1
        for dy in range(Y):
            for dx in range(X):
                if board[y + dy][x + dx] == 0:
                    empty += 1
                    if not black_drop(y + dy, x + dx): return False
                else:
                    if value == -1:
                        value = board[y + dy][x + dx]
                    elif value != board[y + dy][x + dx]:
                        return False
        if empty > 2:
            return False

        for dy in range(Y):
            for dx in range(X):
                board[y+dy][x+dx] = 0
        return True

    answer = 0

    while True:
        update = 0
        for i in range(N):
            for j in range(N):
                if crash(i, j, 2, 3): update += 1
                if crash(i, j, 3, 2): update += 1

        answer += update
        if not update:
            break

    return answer