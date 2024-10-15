import sys
from collections import deque
input = sys.stdin.readline


def bfs(queue):
    visited[queue[0]] = 0
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if visited[next] != -1: continue
            visited[next] = visited[curr] + 1
            queue.append(next)

    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([1])
    visited = [-1] * (N+1)
    bfs(queue)

    rtn1 = visited.index(max(visited))
    rtn2 = visited[rtn1]
    rtn3 = visited.count(max(visited))

    print(rtn1, rtn2, rtn3)
    