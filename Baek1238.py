import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(dist, G):
    heap = [[dist[X], X]]
    while heap:
        dist_curr, curr = heapq.heappop(heap)

        for next, weight in G[curr]:
            if dist_curr + weight < dist[next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, [dist[next], next])
    return


if __name__ == '__main__':
    N, M, X = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    graph_reverse = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append([v, w])
        graph_reverse[v].append([u, w])

    to_destination = [INF] * (N+1)
    to_home = [INF] * (N+1)

    to_destination[X] = 0
    to_home[X] = 0

    dijkstra(to_destination, graph_reverse)
    dijkstra(to_home, graph)

    rtn = 0
    for i in range(1, N+1):
        ans = to_destination[i] + to_home[i]
        rtn = max(rtn, ans)

    print(rtn)
