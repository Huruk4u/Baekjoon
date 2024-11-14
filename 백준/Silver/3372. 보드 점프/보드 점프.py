import sys
input = sys.stdin.readline


def in_range(y, x):
    if (0 <= y < N) and (0 <= x < N):
        return True
    else:
        return False


if __name__ == '__main__':
    N = int(input().strip())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if not matrix[i][j]:
                continue
            if in_range(i + matrix[i][j], j):
                dp[i+matrix[i][j]][j] += dp[i][j]
            if in_range(i, j + matrix[i][j]):
                dp[i][j + matrix[i][j]] += dp[i][j]

    print(dp[N-1][N-1])
