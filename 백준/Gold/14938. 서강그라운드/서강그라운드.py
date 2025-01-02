import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize


if __name__ == '__main__':
    N, M, E = map(int, input().strip().split()) # 노드 갯수, 수색 범위, 엣지 갯수
    items = [0] + list(map(int, input().strip().split()))
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 접근 방식 바꿔서 다익스트라.
    # 각 그래프의 가중치를 최소로 한다고는 해도, BFS가 최소거리 간선을 선택한다는 보장이 없기 때문
    answer = 0
    for i in range(1, N+1):
        dist = [INF] * (N+1)
        heap = [(i, 0)]  # (현재 노드 번호, 탐색한 거리)

        dist[i] = 0
        while heap:
            curr, curr_dist = heapq.heappop(heap)
            if dist[curr] < curr_dist:  # promising하지 않은 경로는 처리
                continue

            for next, weight in graph[curr]:
                new_dist = curr_dist + weight
                if new_dist < dist[next] and new_dist <= M:
                    dist[next] = new_dist
                    heapq.heappush(heap, (next, new_dist))

        # 얻은 아이템의 계산을 따로 했음. 다익스트라는 중복방문의 가능성이 있어서
        item_get = 0
        for i in range(1, N+1):
            if dist[i] != INF:  # 방문한 노드의 경우 아이템 추가
                item_get += items[i]

        answer = max(answer, item_get)

    print(answer)