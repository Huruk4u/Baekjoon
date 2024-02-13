import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    dist[S] = 0
    heap = [[0, start]]
    while heap:
        dist_curr, curr = heapq.heappop(heap)
        for next, weight in graph[curr]:
            if dist_curr + weight < dist[next] and connected[curr][next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, [dist[next], next])

    return


def find_min_edge(start):
    heap = [start]
    while heap:
        curr = heapq.heappop(heap)
        if curr == S:
            continue
        if visited[curr]:
            continue
        visited[curr] = True

        for next, weight in graph_reverse[curr]:
            if dist[next] + weight == dist[curr]:
                heapq.heappush(heap, next)
                connected[next][curr] = False

    return


if __name__ == '__main__':
    while True:
        N, M = map(int, input().strip().split())
        if N == 0 and M == 0:
            break

        S, E = map(int, input().strip().split())
        graph = [[] for _ in range(N)]
        graph_reverse = [[] for _ in range(N)]
        for _ in range(M):
            u, v, w = map(int, input().strip().split())
            graph[u].append([v, w])
            graph_reverse[v].append([u, w])

        dist = [INF] * N
        connected = [[True] * N for _ in range(N)]
        visited = [False] * N

        dijkstra(S)
        find_min_edge(E)

        dist = [INF] * N
        dijkstra(S)

        if dist[E] < INF:
            print(dist[E])
        else:
            print(-1)
