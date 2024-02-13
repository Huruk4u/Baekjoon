import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000001)


def dijkstra(curr):
    print("%d visited" % curr)
    for next, weight in graph[curr]:
        if dist[curr] + weight < dist[next]:
            dist[next] = dist[curr] + weight
            heapq.heappush(heap, (dist[next], next))

    if not heap:
        return
    else:
        dijkstra(heapq.heappop(heap)[1])


if __name__ == '__main__':
    V, E = map(int, input().strip().split())
    start = int(input().strip())
    INF = sys.maxsize

    # graph
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append([v, w])

    dist = [INF] * (V+1)
    dist[start] = 0

    heap = []

    dijkstra(start)

    for i in range(1, V+1):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])
