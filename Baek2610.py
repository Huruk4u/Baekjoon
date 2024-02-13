import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize


def bfs(start):
    rtn = []
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if visited[curr]:
            continue
        visited[curr] = True
        rtn.append(curr)
        for next in graph[curr]:
            if visited[next]:
                continue
            queue.append(next)

    return rtn


def floyd_warshall():
    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                new_dist = dist[u][k] + dist[k][v]
                if new_dist < dist[u][v]:
                    dist[u][v] = new_dist


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    graph = [[] for _ in range(N+1)]
    dist = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)
        dist[a][b] = 1
        dist[b][a] = 1

    # O(N)
    visited = [False] * (N+1)
    comp = []
    for i in range(1, N+1):
        if visited[i]:
            continue
        comp.append(bfs(i))

    # O(N^3)
    floyd_warshall()

    # O(N^2)
    rtn = []
    for c in comp:
        rep = [0, INF]
        for i in c:
            i_dist = 0
            for j in c:
                if i == j:
                    continue
                i_dist = max(i_dist, dist[i][j])
            if i_dist < rep[1]:
                rep = [i, i_dist]
        rtn.append(rep[0])

    rtn.sort()
    print(len(rtn))
    for _ in range(len(rtn)):
        print(rtn[_])