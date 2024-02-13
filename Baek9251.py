import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000001)


def solve(i, j):
    if i >= N and j >= M:
        if string1[i] == string2[j]:
            return 1
        else:
            return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if string1[i] == string2[j]:
        if i >= N or j >= M:
            dp[i][j] = 1
            return dp[i][j]
        else:
            dp[i][j] = solve(i+1, j+1) + 1
    else:
        if i >= N:
            dp[i][j] = solve(i, j+1)
        elif j >= M:
            dp[i][j] = solve(i+1, j)
        else:
            dp[i][j] = max(solve(i+1, j), solve(i, j+1))

    return dp[i][j]


if __name__ == '__main__':
    string1 = input().strip()
    string2 = input().strip()
    N = len(string1) - 1
    M = len(string2) - 1
    # dp[i][j] = string[i], string[j]에서 최대 LCS길이
    dp = [[-1] * (M+1) for _ in range(N+1)]
    print(solve(0, 0))
