import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, T = map(int, input().strip().split())
    dp = [[0] * (T+1) for _ in range(N+1)]
    problem = [list(map(int, input().strip().split())) for _ in range(N)]

    for i in range(1, N+1):
        for k in range(T+1):
            if k - problem[i-1][0] >= 0:
                dp[i][k] = max(dp[i-1][k], dp[i-1][k - problem[i-1][0]] + problem[i-1][1])
            else:
                dp[i][k] = dp[i-1][k]

    print(dp[N][T])