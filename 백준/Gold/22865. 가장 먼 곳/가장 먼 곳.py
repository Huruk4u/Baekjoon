import sys, heapq
input = sys.stdin.readline

INF = sys.maxsize


def dijkstra(heap, dist):
    dist[heap[0][1]] = 0
    while heap:
        dist_curr, curr = heapq.heappop(heap)
        if dist[curr] < dist[curr]: continue

        for next, weight in graph[curr]:
            if dist[next] <= dist_curr + weight: continue
            dist[next] = dist_curr + weight
            heapq.heappush(heap, (dist[next], next))


if __name__ == '__main__':
    N = int(input().strip())
    A, B, C = map(int, input().strip().split())
    M = int(input().strip())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    # A dist
    distA = [INF] * (N+1)
    dijkstra([(0, A)], distA)

    # B dist
    distB = [INF] * (N+1)
    dijkstra([(0, B)], distB)

    # C dist
    distC = [INF] * (N+1)
    dijkstra([(0, C)], distC)

    max_dist, answer = 0, 0
    for i in range(1, N+1):
        temp = min(distA[i], distB[i], distC[i])
        if temp > max_dist:
            max_dist = temp
            answer = i

    print(answer)
