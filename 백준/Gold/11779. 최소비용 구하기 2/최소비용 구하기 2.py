import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(heap):
    while heap:
        curr_cost, curr, path = heapq.heappop(heap)
        if curr == end:
            return curr_cost, path
        if dist[curr] < curr_cost:
            continue

        for next, weight in graph[curr]:
            new_dist = curr_cost + weight
            if new_dist < dist[next]:
                dist[next] = new_dist
                new_path = path[:]
                new_path.append(next)
                heapq.heappush(heap, (new_dist, next, new_path))

    return None, None




if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    dist = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))

    start, end = map(int, input().strip().split())
    dist[start] = 0
    heap = [(0, start, [start])]

    answer, path = dijkstra(heap)

    print(answer)
    print(len(path))
    print(*path)