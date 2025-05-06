import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(heap):
    while heap:
        dist_curr, curr = heapq.heappop(heap)

        if dist[curr] < dist_curr: continue

        for next, weight in graph[curr]:
            if dist[next] <= dist_curr + weight: continue

            dist[next] = dist_curr + weight
            heapq.heappush(heap, (dist[next], next))


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    S, E = map(int, input().strip().split())

    dist = [INF] * (N+1)
    dist[S] = 0

    dijkstra([(0, S)])

    print(dist[E])
