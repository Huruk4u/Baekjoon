import sys
from collections import deque
from pprint import pprint
from copy import deepcopy

input = sys.stdin.readline

def is_edge(a, b):
    code_a = codes[a]
    code_b = codes[b]

    cnt = 0
    for i in range(K):
        if code_a[i] != code_b[i]: cnt += 1

    if cnt == 1: return True
    else: return False

def bfs(queue):
    visited = [False] * (N+1)
    visited[queue[0][0]] = True
    while queue:
        curr, path = queue.popleft()
        if curr == B: return path

        for next in graph[curr]:
            if visited[next]: continue
            visited[next] = True
            next_path = deepcopy(path)
            next_path.append(next)

            queue.append((next, next_path))

    return []



if __name__ == '__main__':
    # input
    N, K = map(int, input().strip().split())
    codes = [[]]
    for _ in range(N):
        codes.append(list(input().strip()))
    A, B = map(int, input().strip().split())
    # input

    # graph
    graph = [[] for _ in range(N+1)]
    for u in range(1, N+1):
        for v in range(u + 1, N+1):
            if u == v: continue
            if is_edge(u, v):
                graph[u].append(v)
                graph[v].append(u)

    queue = deque()
    queue.append((A, [A]))

    answer_path = bfs(queue)
    if not answer_path: print(-1)
    else: print(*answer_path)
