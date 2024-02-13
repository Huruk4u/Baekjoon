import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def solve(curr):
    visited[curr] = 1
    dp[curr][1] = 1
    for friend in tree[curr]:
        if not visited[friend]:
            solve(friend)
            # is early
            dp[curr][1] += min(dp[friend][1], dp[friend][0])
            # not early
            dp[curr][0] += dp[friend][1]


if __name__ == '__main__':
    n = int(input().strip())

    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    dp = [[0, 0] for _ in range(n+1)]
    visited = [0] * (n+1)

    solve(1)

    print(min(dp[1][1], dp[1][0]))
