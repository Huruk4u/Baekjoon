import sys
from collections import deque
input = sys.stdin.readline

def in_range(x):
    return (0 <= x < B+1)


def bfs(queue):
    visited[queue[0]] = 1
    while (queue):
        curr = queue.popleft()
        if curr == B: return visited[curr]

        if in_range(curr*2) and curr*2 not in visited:
            visited[curr*2] = visited[curr] + 1
            queue.append(curr*2)

        if in_range(int(str(curr) + "1")) and int(str(curr) + "1") not in visited:
            visited[int(str(curr) + "1")] = visited[curr] + 1
            queue.append(int(str(curr) + "1"))

    return -1


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    visited = dict()

    print(bfs(deque([A])))