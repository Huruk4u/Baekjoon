import sys
input = sys.stdin.readline
INF = sys.maxsize


def floyd_warshall():
    for k in range(1, V+1):
        for u in range(1, V+1):
            for v in range(1, V+1):
                new_dist = dist[u][k] + dist[k][v]
                if new_dist < dist[u][v]:
                    dist[u][v] = new_dist


if __name__ == '__main__':
    V, E = map(int, input().strip().split())

    dist = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().strip().split())
        dist[a][b] = c

    floyd_warshall()

    # solve
    rtn = INF
    for i in range(1, V+1):
        for j in range(1, V+1):
            if dist[i][j] != INF and dist[j][i] != INF:
                rtn = min(rtn, dist[i][j] + dist[j][i])

    if rtn != INF:
        print(rtn)
    else:
        print(-1)
