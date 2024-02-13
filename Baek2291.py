import sys
input = sys.stdin.readline


def rtn_dp():
    for i in range(1, N+1):
        for j in range(1, M+1):
            print("========================")
            print(i, j)
            if i > j:
                continue
            if i == 1:
                dp[i][j][j//i] = 1
                continue
            for k in range(1, (j//i)+1):
                for t in range(1, len(dp[i-1][j-k])):
                    if t < k:
                        continue
                    dp[i][j][k] += dp[i-1][j-k][t]
                # dp[i][j][k] += sum(dp[i-1][j-k])
                print("dp[%d][%d][%d] = %d, sum of dp[%d][%d]" % (i, j, k, dp[i][j][k], i-1, j-k))


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())

    # dp[n][m][k] = 합이 m인 n길이 수열 중 앞자리가 k인 수열의 개수
    dp = [[[0] for _ in range(M+1)] for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, M+1):
            for _ in range(1, (m//n)+1):
                dp[n][m].append(0)

    print(dp)
    rtn_dp()
    print(dp)