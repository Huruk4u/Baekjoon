import sys

input = sys.stdin.readline

# dx, dy
dj = [-1, 1, 0, 0]
di = [0, 0, -1, 1]


def check_length(idx, check_col):
    cnt = 1
    max_cnt = 1
    if check_col:
        prev_candy = board[idx][0]
        print("prev_candy %s" % prev_candy)
        for k in range(1, n):
            print("comp %s %s" % (board[idx][k], prev_candy))
            print("comp idx = %d %d" % (idx, k))
            if board[idx][k] == prev_candy:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
            prev_candy = board[idx][k]
    else:
        prev_candy = board[0][idx]
        print("prev_candy %s" % prev_candy)
        for y in range(n):
            print(board[y])
        for k in range(1, n):
            print("comp %s %s" % (board[k][idx], prev_candy))
            print("comp idx = %d %d" % (k, idx))
            if board[k][idx] == prev_candy:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
            prev_candy = board[k][idx]
    return max_cnt


def solve():
    ans = 0
    for i in range(n):
        for j in range(n):
            curr_candy = board[i][j]
            print("\n==========================================")
            print("i = %d j = %d candy = %s" % (i, j, curr_candy))
            for t in range(4):
                next_i = i + di[t]
                next_j = j + dj[t]
                if (0 <= next_i < n) and (0 <= next_j < n):
                    if board[next_i][next_j] != curr_candy:
                        print("%s %s change" % (curr_candy, board[next_i][next_j]))
                        print("changing idx = %d %d" % (next_i, next_j))
                        board[i][j], board[next_i][next_j] = board[next_i][next_j], board[i][j]
                        # change row, check column
                        if abs(next_i) == 1:
                            ans = max(check_length(i, False), ans)
                        # change column, check row
                        else:
                            ans = max(check_length(j, True), ans)
                        print("ans = %d" % ans)
                        board[i][j], board[next_i][next_j] = board[next_i][next_j], board[i][j]

    return ans


if __name__ == '__main__':
    # input
    n = int(input().strip())
    board = [list(input().strip()) for _ in range(n)]

    original = 0
    for t in range(n):
        original = max(check_length(t, True), check_length(t, False), original)

    print("original = %d" % original)
    print(solve())