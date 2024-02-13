import sys


def backtracking(row, col):
    global ans, n
    if row == n+1:
        ans += 1
        return
    else:
        for j in range(1, n+1):
            col[row] = j
            if promising(row, col):
                backtracking(row+1, col)


def promising(row, col):
    for r in range(1, row):
        if col[row] == col[r] or abs(col[row] - col[r]) == (row - r):
            return False
    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    queen_pos = [0] * (n+1)
    ans = 0

    backtracking(1, queen_pos)

    print(ans)