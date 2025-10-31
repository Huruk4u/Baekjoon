import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    visited = [-1] * (N+1)
    visited[queue[0]] = 0

    while queue:
        curr = queue.popleft()
        for next in range(N+1):
            if not graph[curr][next] or visited[next] != -1: continue
            visited[next] = visited[curr] + 1
            queue.append(next)

    return visited


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    graph = [[False] * (N+1) for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().strip().split())
        graph[u][v] = True
        graph[v][u] = True

    relation_cnt = [0] * N
    answer = 0
    for k in range(N):
        expanded_edge = set()
        for u in range(1, N+1):
            relation_dist = bfs(deque([u]))
            for v in range(1, N+1):
                if relation_dist[v] == 2:
                    expanded_edge.add((u, v))
                    flag = True

        if not expanded_edge:
            answer = k
            break
        else:
            for u, v in expanded_edge:
                graph[u][v] = True
                relation_cnt[k] += 1

    print(answer)
    for i in range(answer):
        print(relation_cnt[i] // 2)
