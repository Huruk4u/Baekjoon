import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(1, N+1):
        for u in range(1, N+1):
            for v in range(1, N+1):
                new_dist = dist[u][k] + dist[k][v]
                if new_dist < dist[u][v]:
                    dist[u][v] = new_dist


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    dist = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().strip().split())
        dist[a][b] = 1

    floyd_warshall()

    Q = int(input().strip())
    for _ in range(Q):
        i, j = map(int, input().strip().split())
        if dist[i][j] != INF:
            print(-1)
        elif dist[j][i] != INF:
            print(1)
        else:
            print(0)
