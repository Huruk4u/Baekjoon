import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra():
    heap = [[0, 1, K]]
    dist[1][K] = 0
    while heap:
        dist_curr, curr, k = heapq.heappop(heap)
        if dist[curr][k] < dist_curr:
            continue

        for next, weight in graph[curr]:
            if dist_curr + weight < dist[next][k]:
                dist[next][k] = dist_curr + weight
                heapq.heappush(heap, [dist[next][k], next, k])
            if dist_curr < dist[next][k-1] and k >= 1:
                dist[next][k-1] = dist_curr
                heapq.heappush(heap, [dist[next][k-1], next, k-1])

    return


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append([v, w])
        graph[v].append([u, w])

    dist = [[INF] * (K + 1) for _ in range(N + 1)]

    dijkstra()

    print(min(dist[N]))
