import sys
input = sys.stdin.readline


def dfs(curr):
    print("%d visited" % curr)
    rtn = 1
    visited[curr] = True

    for next in graph[curr]:
        if visited[next]:
            continue



if __name__ == '__main__':
    N = int(input().strip())
    n_edges = int(input().strip())

    graph = [[] for _ in range(N+1)]
    for _ in range(n_edges):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N+1)
    print(dfs(1))
