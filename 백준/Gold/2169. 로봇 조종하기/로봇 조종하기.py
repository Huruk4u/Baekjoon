import sys
from pprint import pprint

INF = sys.maxsize
dy, dx = [1, 0, 0], [0, -1, 1]


def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dp = [list(map(int, input().strip().split())) for _ in range(N)]

    for x in range(1, M):
        dp[0][x] += dp[0][x-1]

    for y in range(1, N):
        left_to_right = dp[y][:]    # 상->하, 좌->우 접근
        right_to_left = dp[y][:]    # 상->하, 우->좌 접근

        for x in range(M):
            if x == 0:
                left_to_right[x] += dp[y-1][x]
            else:
                left_to_right[x] += max(dp[y-1][x], left_to_right[x-1])

        for x in range(M-1, -1, -1):
            if x == M-1:
                right_to_left[x] += dp[y-1][x]
            else:
                right_to_left[x] += max(dp[y-1][x], right_to_left[x+1])

        for x in range(M):
            dp[y][x] = max(left_to_right[x], right_to_left[x])

    print(dp[N-1][M-1])