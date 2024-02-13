import sys

input = sys.stdin.readline

# dx, dy
dj = [-1, 1, 0, 0]
di = [0, 0, -1, 1]


def check_height(idx):
    cnt = 1
    max_cnt = 1
    prev_candy = board[0][idx]
    for k in range(1, n):
        if board[k][idx] == prev_candy:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        prev_candy = board[k][idx]
    max_cnt = max(max_cnt, cnt)
    return max_cnt


def check_width(idx):
    max_cnt = 1
    cnt = 1
    prev_candy = board[idx][0]
    for k in range(1, n):
        if board[idx][k] == prev_candy:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
        prev_candy = board[idx][k]
    max_cnt = max(max_cnt, cnt)
    return max_cnt


def solve():
    ans = 0
    for i in range(n):
        for j in range(n-1):
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                # change row, check column
                ans = max(check_width())
                # change column, check row
                else:
                    ans = max(check_length(j, False), ans)
                board[i][j], board[next_i][next_j] = board[next_i][next_j], board[i][j]

    return ans


if __name__ == '__main__':
    # input
    n = int(input().strip())
    board = [list(input().strip()) for _ in range(n)]

    print(solve())
