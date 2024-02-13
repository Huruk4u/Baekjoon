import sys
input = sys.stdin.readline


if __name__ == '__main__':
    dp = [0, 1, 1, 1] + ([0] * 97)
    for i in range(4, 101):
        dp[i] = dp[i-2] + dp[i-3]

    for _ in range(int(input().strip())):
        print(dp[int(input().strip())])
