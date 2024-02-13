# 22/09/19
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
y, x = map(int, sys.stdin.readline().strip().split())
matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(y)]
visited = [[[0, 0] for j in range(x)] for i in range(y)]


def bfs(queue):
    while queue:
        curr_y, curr_x, crush = queue.popleft()
        if curr_x == (x-1) and curr_y == (y-1):
            return visited[curr_y][curr_x][crush]

        for i in range(4):
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]
            if (0 <= next_x < x) and (0 <= next_y < y):
                # 벽이 아닌 경우
                if not matrix[next_y][next_x]:
                    if not visited[next_y][next_x][crush]:
                        queue.append((next_y, next_x, crush))
                        visited[next_y][next_x][crush] = visited[curr_y][curr_x][crush] + 1
                # 벽을 만난 경우
                elif matrix[next_y][next_x] and not crush:
                    queue.append((next_y, next_x, 1))
                    visited[next_y][next_x][1] = visited[curr_y][curr_x][crush] + 1


if __name__ == '__main__':
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    res = bfs(queue)

    if res is None:
        print(-1)
    else:
        print(res)
