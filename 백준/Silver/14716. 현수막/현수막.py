import sys
sys.setrecursionlimit(100000001)

input = sys.stdin.readline
dy, dx = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]


def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


def dfs(cy, cx):
    for i in range(8):
        ny, nx = cy + dy[i], cx + dx[i]
        if not in_range(ny, nx) or visited[ny][nx] or not matrix[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(ny, nx)
    return

if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    answer = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x] or not matrix[y][x]: continue
            answer += 1
            dfs(y, x)

    print(answer)