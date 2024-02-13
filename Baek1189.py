import sys


def bt(i, j, depth):
    global k, cnt
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    if i == 0 and j == n_col-1:
        if depth == k:
            cnt += 1
        return

    for t in range(4):
        next_i = i + di[t]
        next_j = j + dj[t]
        if (0 <= next_i < n_row) and (0 <= next_j < n_col):
            if not vst[next_i][next_j] and matrix[next_i][next_j] != 'T':
                vst[next_i][next_j] = True
                bt(next_i, next_j, depth+1)
                vst[next_i][next_j] = False


if __name__ == '__main__':
    # input
    n_row, n_col, k = map(int, sys.stdin.readline().strip().split())
    matrix = [list(sys.stdin.readline().strip()) for _ in range(n_row)]

    vst = [[False] * n_col for _ in range(n_row)]
    cnt = 0

    bt(n_row, 0, 0)

    print(cnt)
