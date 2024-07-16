from pprint import pprint
from collections import deque


def solution(rectangle, cx, cy, itemX, itemY):

    def expand(x):
        return x * 2

    def in_range(y, x):
        if (0 <= y < 102) and (0 <= x < 102):
            return True
        else:
            return False

    def bfs(queue):
        visited[queue[0][0]][queue[0][1]] = 1
        while queue:
            cy, cx = queue.popleft()
            if cy == itemY and cx == itemX:
                return visited[cy][cx] - 1
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if not in_range(ny, nx) or visited[ny][nx] or not matrix[ny][nx]:
                    continue
                queue.append((ny, nx))
                visited[ny][nx] = visited[cy][cx] + 1
        return 0

    matrix = [[0 for _ in range(102)] for _ in range(102)]
    cx, cy, itemX, itemY = map(expand, (cx, cy, itemX, itemY))
    for i in range(1, len(rectangle) + 1):
        sx, sy, ex, ey = map(expand, rectangle[i-1])
        for y in range(sy, ey + 1):
            matrix[y][sx] = 1
            matrix[y][ex] = 1
        for x in range(sx, ex + 1):
            matrix[sy][x] = 1
            matrix[ey][x] = 1

    for sx, sy, ex, ey in rectangle:
        for y in range(sy * 2 + 1, ey * 2):
            for x in range(sx * 2 + 1, ex * 2):
                matrix[y][x] = 0

    visited = [[0 for _ in range(102)] for _ in range(102)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = bfs(deque([(cy, cx)])) // 2

    return answer
