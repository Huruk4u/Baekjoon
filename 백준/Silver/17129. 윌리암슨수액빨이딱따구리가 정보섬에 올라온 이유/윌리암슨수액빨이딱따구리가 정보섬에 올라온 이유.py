import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs(queue) :
    while queue:
        cy, cx = queue.popleft()
        if matrix[cy][cx] in ['3', '4', '5']:
            return matrix[cy][cx], visited[cy][cx]

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx) or visited[ny][nx] != -1 or matrix[ny][nx] == '1': continue

            visited[ny][nx] = visited[cy][cx] + 1
            queue.append((ny, nx))

    return '-1', -1


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(input().strip()) for _ in range(N)]

    sy, sx = 0, 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == '2': sy, sx = y, x

    queue = deque()
    queue.append((sy, sx))

    visited = [[-1] * M for _ in range(N)]
    visited[sy][sx] = 0

    eat, dist = bfs(queue)
    if eat == '-1': print("NIE")
    else:
        print("TAK")
        print(dist)
