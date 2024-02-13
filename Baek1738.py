import sys
input = sys.stdin.readline
INF = sys.maxsize


def bf(start):
    dist[start] = 0
    for i in range(1, N+1):
        for s in range(1, N+1):
            for e, c in graph[s]:
                if dist[s] == -INF:
                    continue
                if dist[s] + c > dist[e]:
                    dist[e] = dist[s] + c
                    path[e] = s

                    if i == N:
                        dist[e] = INF
    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append([v, w])

    dist = [-INF] * (N+1)
    path = [0] * (N+1)

    bf(1)

    rtn = [N]
    if dist[N] == INF:
        print(-1)
    else:
        node = N
        while node != 1:
            node = path[node]
            rtn.append(node)

        rtn.reverse()
        print(*rtn)
