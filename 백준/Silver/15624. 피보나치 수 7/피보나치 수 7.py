import sys
input = sys.stdin.readline
MOD = 1000000007


if __name__ == '__main__':
    N = int(input().strip())
    if N == 0 or N == 1:
        print(N)
    else:
        dp = [0] * (N+1)
        dp[1], dp[2] = 1, 1
        for i in range(3, N+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD

        print(dp[N])
