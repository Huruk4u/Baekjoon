import sys, heapq
input = sys.stdin.readline


def dijkstra():
    while heap:
        dist_curr, curr = heapq.heappop(heap)
        if curr == end:
            return dist[end]

        for next, weight in graph[curr]:
            if dist_curr + weight < dist[next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, (dist[next], next))

    return dist[end]


if __name__ == '__main__':
    N = int(input().strip())
    E = int(input().strip())
    INF = sys.maxsize

    # graph
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append([v, w])

    start, end = map(int, input().strip().split())

    dist = [INF] * (N+1)
    dist[start] = 0

    heap = []
    heapq.heappush(heap, (dist[start], start))

    print(dijkstra())
