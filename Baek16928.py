import sys, heapq
input = sys.stdin.readline


def bfs(heap):
    rtn = sys.maxsize
    while heap:
        dice_cnt, curr = heapq.heappop(heap)
        if curr == 100:
            rtn = min(rtn, dice_cnt)

        for next in graph[curr]:
            if snakeLadder[curr]:
                heapq.heappush(heap, (dice_cnt, next))
            else:
                if visited[next]:
                    continue
                visited[next] = 1
                heapq.heappush(heap, (dice_cnt+1, next))

    return rtn


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(101)]
    snakeLadder = [False for _ in range(101)]

    for _ in range(N+M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        snakeLadder[u] = True

    for i in range(1, 101):
        if graph[i]:
            continue
        for j in range(1, 7):
            if (i+j) > 100:
                continue
            graph[i].append(i+j)

    visited = [0 for _ in range(101)]
    visited[1] = 1
    heap = []
    heapq.heappush(heap, (0, 1))

    print(bfs(heap))
