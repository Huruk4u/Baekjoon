import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra():
    # [distance of #, curr node #, prev node #]
    heap = [[dist[1], 1, 0]]
    rtn = []
    while heap:
        dist_curr, curr, prev = heapq.heappop(heap)

        if visited[curr]:
            continue
        visited[curr] = True

        if prev:
            rtn.append((prev, curr))

        for next, weight in graph[curr]:
            if dist_curr + weight < dist[next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, [dist[next], next, curr])

    return rtn


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B, C = map(int, input().strip().split())
        graph[A].append([B, C])
        graph[B].append([A, C])

    dist = [INF] * (N+1)
    dist[1] = 0

    visited = [False] * (N+1)

    rtn = dijkstra()

    print(len(rtn))
    for i in range(len(rtn)):
        print("%d %d" % (rtn[i][0], rtn[i][1]))
