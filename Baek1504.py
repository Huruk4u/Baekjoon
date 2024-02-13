import sys, heapq
input = sys.stdin.readline


def dijkstra(start, dist):
    heap = [[0, start]]
    dist[start] = 0
    while heap:
        dist_curr, curr = heapq.heappop(heap)

        for next, weight in graph[curr]:
            # 갈 수 없는 경로면 continue
            if weight == INF:
                continue
            if dist_curr + weight < dist[next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, [dist[next], next])

    return


if __name__ == '__main__':
    N, E = map(int, input().strip().split())
    INF = sys.maxsize

    # graph[Node][2] = [node #, edge_weight]
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, input().strip().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    u, v = map(int, input().strip().split())

    # solve
    dist_1 = [INF] * (N+1)
    dist_u = [INF] * (N+1)
    dist_v = [INF] * (N+1)

    dijkstra(1, dist_1)
    dijkstra(u, dist_u)
    dijkstra(v, dist_v)

    suvN = dist_1[u] + dist_u[v] + dist_v[N]
    svuN = dist_1[v] + dist_v[u] + dist_u[N]

    rtn = min(suvN, svuN)
    if rtn >= INF:
        print(-1)
    else:
        print(min(suvN, svuN))
