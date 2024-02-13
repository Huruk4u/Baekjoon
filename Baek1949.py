import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def good_town(curr, selected):
    if dp[curr][selected]:
        return dp[curr][selected]

    visited[curr][selected] = 1
    print("%d visited" % curr)
    print("visited[%d][%d] = %d" % (curr, selected, visited[curr][selected]))
    if selected:
        if not tree[curr]:  # leaf node
            return weight[curr]
        for next_town in tree[curr]:
            print("visited[%d][%d] = %d" % (next_town, selected, visited[next_town][selected]))
            if not visited[next_town][0]:
                dp[curr][selected] = max(good_town(next_town, 0), dp[curr][selected])
                print("\n============================== curr = %d selected==============================" % curr)
                print("dp[curr][1] = %d" % dp[curr][selected])

    else:
        if not tree[curr]:  # leaf node
            return 0
        for next_town in tree[curr]:
            print("visited[%d][%d] = %d" % (next_town, selected, visited[next_town][selected]))
            if not visited[next_town][0]:
                dp[curr][selected] = max(weight[curr] + good_town(next_town, 0), dp[curr][selected])
            if not visited[next_town][1]:
                dp[curr][selected] = max(weight[curr] + good_town(next_town, 1), dp[curr][selected])
                print("\n============================== curr = %d not selected ==============================" % curr)
                print("dp[curr][0] = %d" % dp[curr][selected])

    return dp[curr][selected]


if __name__ == '__main__':
    n = int(input().strip())
    weight = [0] + list(map(int, input().strip().split()))

    # tree
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    # visited
    visited = [[0, 0] for _ in range(n+1)]
    print(visited)
    # dp[n] = n번 마을 선정 시, 최대 합
    dp = [[0, 0] for _ in range(n+1)]

    ans = max(good_town(1, 0), good_town(1, 1))
    print(ans)
