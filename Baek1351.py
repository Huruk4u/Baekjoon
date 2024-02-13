import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def solve(x):
    if x == 0:
        return dp[0]
    if x in visited:
        return dp[x]

    visited.add(x)

    dp[x] = solve(x//p) + solve(x//q)
    return dp[x]


if __name__ == '__main__':
    n, p, q = map(int, input().strip().split())
    dp = dict()
    dp[0] = 1
    visited = set()

    solve(n)

    print(dp[n])
