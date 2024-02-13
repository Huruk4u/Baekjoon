import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline


def dfs(p, curr):
    parent[curr] = p
    visited[curr] = True

    for next_node in graph[curr]:
        if not visited[next_node]:
            dfs(curr, next_node)


if __name__ == '__main__':
    n = int(input().strip())

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (n+1)
    visited = [False] * (n+1)

    dfs(0, 1)

    for ans in range(2, n+1):
        print(parent[ans])
