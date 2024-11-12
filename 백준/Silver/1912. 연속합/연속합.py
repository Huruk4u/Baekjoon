import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    dp = list(map(int, input().strip().split()))
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i-1] + dp[i])

    print(max(dp))
