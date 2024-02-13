import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))

    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[j] + 1, dp[i])

    print(max(dp))
