import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


def bfs(queue):
    visited[queue[0][0]][queue[0][1]][queue[0][2]] = 1
    while queue:
        cy, cx, cd = queue.popleft()
        if cy == ey and cx == ex:
            return visited[cy][cx][cd] - 1

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx): continue
            if matrix[ny][nx]:
                if cd or visited[ny][nx][cd + 1]: continue
                queue.append((ny, nx, cd + 1))
                visited[ny][nx][cd + 1] = visited[cy][cx][cd] + 1
            else:
                if visited[ny][nx][cd]: continue
                queue.append((ny, nx, cd))
                visited[ny][nx][cd] = visited[cy][cx][cd] + 1
    return -1


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    sy, sx = map(int, input().strip().split())
    ey, ex = map(int, input().strip().split())

    sy, sx = sy - 1, sx - 1
    ey, ex = ey - 1, ex - 1

    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = deque([(sy, sx, 0)])
    print(bfs(queue))
