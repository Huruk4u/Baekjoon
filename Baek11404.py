import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        s, e, w = map(int, input().strip().split())
        dist[s][e] = min(dist[s][e], w)

    floyd_warshall()
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] == INF or i == j:
                dist[i][j] = 0

    for i in range(1, N+1):
        print(*dist[i][1:])

