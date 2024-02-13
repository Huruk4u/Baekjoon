import sys


def solve(n):
    if dp[n]:
        return dp[n]
    if (n % 2) == 1:
        return 0
    else:
        dp[n] = solve(n-2) * 3
        for i in range(n-2, 2, -2):
            dp[n] += solve(n-i) * 2
        dp[n] += 2

    return dp[n]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    dp = [0] * (n+1)

    if n == 1:
        print(0)
    else:
        dp[2] = 3

        print(solve(n))
