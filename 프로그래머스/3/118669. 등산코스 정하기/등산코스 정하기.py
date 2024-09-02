import sys, heapq
INF = sys.maxsize


def solution(N, edge, gates, summits):

    def bfs(heap):
        while heap:
            intensity, curr = heapq.heappop(heap)
            if is_summit[curr] or dist[curr] < intensity:
                continue
                
            for next, weight in graph[curr]:
                new_dist = max(weight, dist[curr])
                if dist[next] > new_dist:
                    dist[next] = new_dist
                    heapq.heappush(heap, (dist[next], next))
        return

    # 그래프 정리
    graph = [[] for _ in range(N + 1)]
    for u, v, w in edge:
        graph[u].append((v, w))
        graph[v].append((u, w))

    is_summit = [False] * (N + 1)
    for summit in summits:
        is_summit[summit] = True

    dist = [INF] * (N+1)
    heap = []
    for gate in gates:
        dist[gate] = 0
        heapq.heappush(heap, (0, gate))

    bfs(heap)

    answer = [0, INF]
    summits.sort()
    for summit in summits:
        if dist[summit] < answer[1]:
            answer = [summit, dist[summit]]

    return answer