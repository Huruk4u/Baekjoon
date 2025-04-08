import sys
from pprint import pprint

input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dist = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1): dist[i][i] = 0
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        dist[u][v] = w


    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                if dist[u][v] <= dist[u][k] + dist[k][v]:
                    continue
                dist[u][v] = dist[u][k] + dist[k][v]

    K = int(input().strip())
    pivot = list(map(int, input().strip().split()))

    min_dist = INF
    for i in range(1, N+1):
        temp = 0
        for k in pivot: temp = max(temp, dist[i][k] + dist[k][i])
        min_dist = min(min_dist, temp)

    rtn = []
    for i in range(1, N+1):
        temp = 0
        for k in pivot: temp = max(temp, dist[i][k] + dist[k][i])
        if temp == min_dist: rtn.append(i)

    print(*rtn)