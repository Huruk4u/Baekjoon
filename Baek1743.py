# 22/09/01
import sys

sys.setrecursionlimit(10001)


def dfs(x, y):
    global depth
    is_visit[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if (0 <= _x < n) and (0 <= _y < m):
            if prog[_x][_y]:
                if not is_visit[_x][_y]:
                    depth += 1
                    dfs(_x, _y)


n, m, k = map(int, sys.stdin.readline().strip().split())
is_visit = [[False] * m for _ in range(n)]
prog = [[False] * m for _ in range(n)]
vertex = []
for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())
    vertex.append([a - 1, b - 1])
    prog[a - 1][b - 1] = True

res = 1
for x, y in vertex:
    depth = 1
    if not is_visit[x][y]:
        dfs(x, y)
        res = max(res, depth)

print(res)