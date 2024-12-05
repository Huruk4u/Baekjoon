import sys

input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(1, N + 1):
        for u in range(1, N + 1):
            for v in range(1, N + 1):
                new_dist = dist[u][k] + dist[k][v]
                if new_dist < dist[u][v]:
                    dist[u][v] = new_dist


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().strip().split())
        dist[a][b] = 1
        dist[b][a] = 1

    floyd_warshall()

    ans = (0, INF)
    for i in range(1, N + 1):
        kevin = 0
        for j in range(1, N + 1):
            if dist[i][j] == INF:
                continue
            kevin += dist[i][j]

        if kevin < ans[1]:
            ans = (i, kevin)

    print(ans[0])
