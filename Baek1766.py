import sys, heapq
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    inDeg = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        inDeg[b] += 1

    heap = []

    for i in range(1, N+1):
        if not inDeg[i]:
            heapq.heappush(heap, i)

    rtn = []
    while heap:
        curr = heapq.heappop(heap)
        rtn.append(curr)
        for next in graph[curr]:
            inDeg[next] -= 1
            if not inDeg[next]:
                heapq.heappush(heap, next)

    print(*rtn)
