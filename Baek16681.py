import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start, dist):
    dist[start] = 0
    heap = [(dist[start], start)]
    while heap:
        dist_curr, curr = heapq.heappop(heap)

        if dist[curr] < dist_curr:
            continue

        for next, weight in graph[curr]:
            # 현재 노드 높이가 다음 노드 높이보다 낮아야만 진행 가능
            if height[curr] >= height[next]:
                continue
            if dist_curr + weight < dist[next]:
                dist[next] = dist_curr + weight
                heapq.heappush(heap, (dist[next], next))

    return


if __name__ == '__main__':
    N, M, D, E = map(int, input().strip().split())

    height = [0] + list(map(int, input().strip().split()))
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    # 현재 위치 ----> 목표 지점
    dist_to_destination = [INF] * (N + 1)
    dijkstra(1, dist_to_destination)

    # 목표 지점 ----> 학교 (역으로 계산)
    dist_to_school = [INF] * (N + 1)
    dijkstra(N, dist_to_school)

    # solve
    rtn = []
    for i in range(2, N):
        total_dist = dist_to_destination[i] + dist_to_school[i]
        if total_dist >= INF:
            continue

        rtn.append((height[i] * E) - (total_dist * D))

    if rtn:
        print(max(rtn))
    else:
        print("Impossible")
