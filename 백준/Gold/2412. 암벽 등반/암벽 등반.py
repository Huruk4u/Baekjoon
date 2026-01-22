import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    while queue:
        cx, cy = queue.popleft()
        if cy == T: return visited[(cx, cy)]

        for next in graph[(cx, cy)]:
            if visited[next] != -1: continue
            visited[next] = visited[(cx, cy)] + 1
            queue.append((next))
    return -1


if __name__ == '__main__':
    N, T = map(int, input().strip().split())
    graph = dict()
    visited = dict()

    graph[(0, 0)] = []
    visited[(0, 0)] = 0
    for _ in range(N):
        x, y = map(int, input().strip().split())
        graph[(x, y)] = []
        visited[(x, y)] = -1

    for x, y in graph.keys():
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if not (x + dx, y + dy) in graph: continue
                graph[(x, y)].append((x + dx, y + dy))

    queue = deque()
    queue.append((0, 0))

    print(bfs(queue))
