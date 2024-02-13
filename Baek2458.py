import sys
input = sys.stdin.readline


def dfs(c):
    visited[c] = True
    for n in graph[c]:
        if visited[n]:
            continue
        small[n] += 1
        dfs(n)


def dfs_rev(c):
    visited_rev[c] = True
    for n in graph_rev[c]:
        if visited_rev[n]:
            continue
        tall[n] += 1
        dfs_rev(n)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N + 1)]
    graph_rev = [[] for _ in range(N + 1)]

    small = [0] * (N + 1)
    tall = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph_rev[b].append(a)

    checked = [False] * (N+1)
    for i in range(1, N+1):
        if checked[i]:
            continue
        visited = [False] * (N+1)
        dfs(i)

        visited_rev = [False] * (N+1)
        dfs_rev(i)

    rtn = 0
    for k in range(1, N+1):
        if tall[k] + small[k] == N-1:
            rtn += 1

    print(rtn)