import sys
input = sys.stdin.readline


def solve(i, j, k):
    # 찾으려는 수가 만들어질 수 있는 문자열 갯수보다 많을 경우 -1 return
    if k > dp[i][j]:
        return '-1'
    else:
        # bottom case
        if i == 0 or j == 0:
            if i == 0:
                return 'z' * j
            else:
                return 'a' * i

        if k <= dp[i-1][j]:
            return 'a' + solve(i-1, j, k)
        else:
            return 'z' + solve(i, j-1, k-dp[i-1][j])


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())

    # dp[i][j] = a의 개수 i, z의 개수 j에서 만들어질 수 있는 문자열의 개수
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(M+1):
            if i == 0 and j == 0:
                dp[i][j] = 0
                continue
            if i == 0 or j == 0:
                dp[i][j] = 1
                continue
            if i == 1 or j == 1:
                dp[i][j] = i + j
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for a in range(1, N+1):
        for b in range(1, M+1):
            print("---------- i = %d, j = %d ----------" % (a, b))
            for c in range(1, dp[a][b]+1):
                print("%d번째 문자열 = %s" % (c, solve(a, b, c)))
