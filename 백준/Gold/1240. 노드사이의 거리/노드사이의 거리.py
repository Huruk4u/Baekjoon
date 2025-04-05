import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(heap, start):
    while heap:
        dist_curr, curr = heapq.heappop(heap)
        if dist[start][curr] < dist_curr: continue

        for next, weight in graph[curr]:
            if dist[start][next] <= dist_curr + weight: continue
            dist[start][next] = dist_curr + weight
            heapq.heappush(heap, (dist[start][next], next))
    return

if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dist[i][i] = 0
        dijkstra([(0, i)], i)

    for _ in range(M):
        u, v = map(int, input().strip().split())
        print(dist[u][v])
