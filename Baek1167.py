import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def dfs(curr):
    child_heap = []
    diameter_heap = []
    visited[curr] = True
    for child, weight in graph[curr]:
        if not visited[child]:
            child_rtn, diameter = dfs(child)
            heapq.heappush(child_heap, -(child_rtn + weight))
            heapq.heappush(diameter_heap, -diameter)

    if not child_heap:
        rtn = 0
        max_diameter = 0
    elif len(child_heap) == 1:
        rtn = -child_heap[0]
        max_diameter = max(-child_heap[0], -diameter_heap[0])
    else:
        rtn = -child_heap[0]
        curr_dia = -(heapq.heappop(child_heap) + heapq.heappop(child_heap))
        max_diameter = max(curr_dia, -diameter_heap[0])

    return rtn, max_diameter


if __name__ == '__main__':
    V = int(input().strip())
    ipt = []
    graph = [[] for _ in range(V+1)]
    for _ in range(V):
        ipt = list(map(int, input().strip().split()))
        vn = ipt[0]
        for i in range(1, len(ipt), 2):
            if ipt[i] == -1:
                break
            graph[vn].append([ipt[i], ipt[i+1]])

    visited = [False] * (V+1)

    g, ans = dfs(1)
    print(ans)
