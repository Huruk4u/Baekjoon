import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    item = [[0, 0]] + [list(map(int, input().strip().split())) for _ in range(N)]
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        weight = item[i][0]
        value = item[i][1]
        for size in range(1, K+1):
            if size >= weight:
                dp[i][size] = max(dp[i-1][size], dp[i-1][size-weight] + value)
            else:
                dp[i][size] = dp[i-1][size]

    print(dp[N][K])
