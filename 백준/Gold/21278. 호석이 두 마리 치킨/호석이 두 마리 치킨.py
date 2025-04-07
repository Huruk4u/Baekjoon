import sys
from pprint import pprint

input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    dist = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1): dist[i][i] = 0
    for _ in range(M):
        u, v = map(int, input().strip().split())
        dist[u][v] = 1
        dist[v][u] = 1

    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                if dist[u][v] <= dist[u][k] + dist[k][v]: continue
                dist[u][v] = dist[u][k] + dist[k][v]

    temp = 0
    node1, node2, min_dist = 0, 0, INF
    for u in range(1, N):
        for v in range(u + 1, N+1):
            temp = 0
            for k in range(1, N+1):
                temp += min(dist[u][k], dist[v][k]) * 2
            if temp < min_dist:
                node1, node2, min_dist = u, v, temp

    print(node1, node2, min_dist)