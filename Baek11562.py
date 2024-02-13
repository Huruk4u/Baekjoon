import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    dist = [[INF] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        u, v, b = map(int, input().strip().split())
        # 양방향 간선인 경우
        if b:
            dist[u][v] = 0
            dist[v][u] = 0
        # 단방향 간선인 경우
        else:
            dist[u][v] = 0
            dist[v][u] = 1

    floyd_warshall()

    for c in range(N+1):
        dist[c][c] = 0

    K = int(input().strip())
    for _ in range(K):
        s, e = map(int, input().strip().split())
        print(dist[s][e])
