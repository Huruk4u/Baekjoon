import sys
input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    dist = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dist[i][i] = 0

    for _ in range(M):
        u, v = map(int, input().strip().split())
        dist[u][v] = 1

    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    for u in range(1, N+1):
        cnt = 0
        for v in range(1, N+1):
            if dist[u][v] != INF or dist[v][u] != INF:
                continue
            cnt += 1
        print(cnt)
