import sys
from collections import deque
input = sys.stdin.readline


def pprint(matrix):
    for _ in range(N):
        print(matrix[_])
    return


def in_range(y, x):
    if (0 <= x < M) and (0 <= y < N):
        return True
    else:
        return False


def bfs(queue, visited):
    visited[queue[0][0]][queue[0][1]] = 1
    melting = set()
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx): continue
            # 다음 영역이 치즈라면
            if matrix[ny][nx]:
                visited[ny][nx] += 1
                if visited[ny][nx] >= 2:
                    melting.add((ny, nx))
            # 다음 영역이 공기라면
            else:
                if visited[ny][nx]: continue
                visited[ny][nx] = 1
                queue.append((ny, nx))
    return melting


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    time = 0
    while True:
        queue = deque([(0, 0)])
        visited = [[0] * M for _ in range(N)]
        melting = bfs(queue, visited)

        if not melting:
            break

        time += 1
        for y, x in melting:
            matrix[y][x] = 0

    print(time)