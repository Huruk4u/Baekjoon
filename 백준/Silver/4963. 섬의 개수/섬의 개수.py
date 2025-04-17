import sys
from collections import deque
input = sys.stdin.readline


dy, dx = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]

def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


def bfs(queue):
    visited[queue[0][0]][queue[0][1]] = True
    while queue:
        cy, cx = queue.popleft()
        for i in range(8):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx): continue
            if not matrix[ny][nx] or visited[ny][nx]: continue
            visited[ny][nx] = True
            queue.append((ny, nx))
    return


if __name__ == '__main__':
    while True:
        M, N = map(int, input().strip().split())
        if N == 0 and M == 0: break

        matrix = [list(map(int, input().strip().split())) for _ in range(N)]
        visited = [[False] * M for _ in range(N)]
        cnt = 0
        for y in range(N):
            for x in range(M):
                if visited[y][x] or not matrix[y][x]: continue
                bfs(deque([(y, x)]))
                cnt += 1

        print(cnt)
