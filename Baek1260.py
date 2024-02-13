# 22/09/13
import sys
from collections import deque


def dfs(current_node):
    visited_dfs[current_node] = True
    res_dfs.append(current_node)
    for next_node in graph[current_node]:
        if not visited_dfs[next_node]:
            dfs(next_node)


def bfs(current_node):
    queue = deque([current_node])

    while queue:
        current_node = queue.popleft()
        visited_bfs[current_node] = True
        res_bfs.append(current_node)
        for next_node in graph[current_node]:
            if not visited_bfs[next_node]:
                if next_node not in queue:
                    queue.append(next_node)


if __name__ == '__main__':
    n_node, n_edge, start_node = map(int,sys.stdin.readline().strip().split())
    graph = [[] for _ in range(n_node+1)]
    for i in range(n_edge):
        a, b = map(int,sys.stdin.readline().strip().split())
        graph[b].append(a)
        graph[a].append(b)

    for j in range(n_node+1):
        graph[j].sort()

    # Dfs
    visited_dfs = [False] * (n_node+1)
    res_dfs = []
    dfs(start_node)
    print(*res_dfs)

    # Bfs
    visited_bfs = [False] * (n_node+1)
    res_bfs = []
    bfs(start_node)
    print(*res_bfs)
