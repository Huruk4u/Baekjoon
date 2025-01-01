import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def in_range(x):
    if 0 <= x < 100001:
        return True
    else:
        return False


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    queue = deque([N])
    dist = [INF] * 100001  # 방문 횟수
    visited = [0] * 100001

    dist[N], visited[N] = 0, 1
    while queue:
        curr = queue.popleft()
        if dist[curr] > dist[K]:
            continue
        if curr == K:
            continue

        if in_range(curr - 1) and dist[curr - 1] >= dist[curr] + 1:
            visited[curr - 1] += 1
            dist[curr - 1] = dist[curr] + 1
            queue.append(curr - 1)
        if in_range(curr + 1) and dist[curr + 1] >= dist[curr] + 1:
            visited[curr + 1] += 1
            dist[curr + 1] = dist[curr] + 1
            queue.append(curr + 1)
        if in_range(curr * 2) and dist[curr * 2] >= dist[curr] + 1:
            visited[curr * 2] += 1
            dist[curr * 2] = dist[curr] + 1
            queue.append(curr * 2)

    print(dist[K])
    print(visited[K])

