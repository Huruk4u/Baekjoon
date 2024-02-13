import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[] for _ in range(N+1)]
    inDeg = [0 for _ in range(N+1)]     # i번째 노드로 향하는 간선의 개수

    # 100,000
    for _ in range(M):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        inDeg[b] += 1

    rtn = []
    queue = deque([])

    # 32000
    for i in range(1, N + 1):
        if not inDeg[i]:
            queue.append(i)
            inDeg[i] -= 1

    while queue:
        curr = queue.popleft()
        rtn.append(curr)
        for next in graph[curr]:
            inDeg[next] -= 1
            if not inDeg[next]:
                queue.append(next)

    print(*rtn)
