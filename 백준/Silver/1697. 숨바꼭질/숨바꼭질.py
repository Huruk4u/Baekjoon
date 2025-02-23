import sys
from collections import deque
input = sys.stdin.readline


def bfs(queue):
    while True:
        curr = queue.popleft()
        if curr == end:
            return visited[curr]

        if in_range(curr - 1):
            if not visited[curr - 1]:
                queue.append(curr - 1)
                visited[curr - 1] = visited[curr] + 1
        if in_range(curr + 1):
            if not visited[curr + 1]:
                queue.append(curr + 1)
                visited[curr + 1] = visited[curr] + 1
        if in_range(curr * 2):
            if not visited[curr * 2]:
                queue.append(curr * 2)
                visited[curr * 2] = visited[curr] + 1


def in_range(x):
    if (0 <= x <= 100000):
        return True
    else:
        return False


if __name__ == '__main__':
    start, end = map(int, input().strip().split())

    queue = deque()
    queue.append(start)
    visited = [0 for _ in range(100001)]

    print(bfs(queue))
    