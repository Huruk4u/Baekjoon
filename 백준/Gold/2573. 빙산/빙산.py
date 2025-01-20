import copy
import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    if (0 <= y < N) and (0 <= x < M):
        return True
    else:
        return False


def bfs(queue):
    visited[queue[0][0]][queue[0][1]] = True
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx) or visited[ny][nx]:
                continue
            if matrix[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return


def melting(queue):
    visited[queue[0][0]][queue[0][1]] = True
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx) or visited[ny][nx]:
                continue
            if matrix[ny][nx]:
                new_matrix[ny][nx] = max(new_matrix[ny][nx] - 1, 0)
            else:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    time = 0
    while True:
        visited = [[False] * M for _ in range(N)]
        cnt = 0
        # 두 컴포넌트 검사
        for y in range(N):
            for x in range(M):
                if not visited[y][x] and matrix[y][x]:
                    # 컴포넌트가 두 개인 경우
                    if cnt >= 2:
                        break
                    bfs(deque([(y, x)]))
                    cnt += 1
        if cnt != 1:
            break

        time += 1
        new_matrix = copy.deepcopy(matrix)
        visited = [[False] * M for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if not visited[y][x] and not matrix[y][x]:
                    melting(deque([(y, x)]))

        matrix = new_matrix

    if not cnt:
        print(0)
    else:
        print(time)