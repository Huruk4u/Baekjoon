import sys
from collections import deque
input = sys.stdin.readline


def in_range(h, y, x):
    if (0 <= h < H) and (0 <= y < M) and (0 <= x < N):
        return True
    else:
        return False


def bfs(queue):
    while queue:
        ch, cy, cx = queue.popleft()
        for i in range(6):
            nh = ch + dh[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            if not in_range(nh, ny, nx):
                continue
            if not visited[nh][ny][nx] and tomato[nh][ny][nx] == 0:
                queue.append((nh, ny, nx))
                visited[nh][ny][nx] = visited[ch][cy][cx] + 1
    return


def get_return():
    rtn = 0
    for h in range(H):
        for y in range(M):
            for x in range(N):
                if tomato[h][y][x] == 0 and visited[h][y][x] == 0:
                    return 0
                rtn = max(rtn, visited[h][y][x])

    return rtn


if __name__ == '__main__':
    N, M, H = map(int, input().strip().split())
    tomato = [[list(map(int, input().strip().split())) for _ in range(M)] for _ in range(H)]

    dx = [0, 0, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, 0, 0]
    dh = [-1, 1, 0, 0, 0, 0]

    visited = [[[0] * N for _ in range(M)] for _ in range(H)]
    queue = deque()
    for h in range(H):
        for y in range(M):
            for x in range(N):
                if tomato[h][y][x] == 1:
                    visited[h][y][x] = 1
                    queue.append((h, y, x))

    bfs(queue)

    print(get_return() - 1)
