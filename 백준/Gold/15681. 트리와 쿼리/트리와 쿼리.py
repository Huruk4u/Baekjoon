import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def dfs(curr):
    subtree_size[curr] = 1

    for next in graph[curr]:
        if subtree_size[next] != -1:
            continue
        subtree_size[curr] += dfs(next)

    return subtree_size[curr]

if __name__ == '__main__':
    N, R, Q = map(int, input().strip().split())

    subtree_size = [-1] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    dfs(R)

    for _ in range(Q):
        print(subtree_size[int(input().strip())])
