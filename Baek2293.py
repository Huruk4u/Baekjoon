import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    dp = [1] + [0] * k
    for _ in range(n):
        value = int(input().strip())
        for i in range(k+1):
            if i - value < 0:
                continue
            dp[i] += dp[i-value]

    print(dp[k])
