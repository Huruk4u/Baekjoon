import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def good_town(curr):
    visited[curr] = 1
    dp[curr][1] = weight[curr]
    for next_town in town[curr]:
        if not visited[next_town]:
            good_town(next_town)
            dp[curr][0] += max(dp[next_town][0], dp[next_town][1])
            dp[curr][1] += dp[next_town][0]


if __name__ == '__main__':
    n = int(input().strip())
    weight = [0] + list(map(int, input().strip().split()))

    town = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().strip().split())
        town[a].append(b)
        town[b].append(a)

    visited = [False] * (n+1)
    dp = [[0, 0] for _ in range(n+1)]

    good_town(1)

    print(max(dp[1][0], dp[1][1]))
