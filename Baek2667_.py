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
        if (0 <= _x < n) and (0 <= _y < n):
            if not is_visit[_x][_y] and [_x,_y] in vertex:
                depth += 1
                dfs(_x, _y)


n = int(sys.stdin.readline().strip())
vertex = []
is_visit = [[False] * n for _ in range(n)]

# main
for y in range(n):
    a = list(sys.stdin.readline().strip())
    for x in range(n):
        if a[x] == '1':
            vertex.append([x, y])

res = []
for x, y in vertex:
    if not is_visit[x][y]:
        depth = 1
        dfs(x, y)
        res.append(depth)
    else:
        continue

res = sorted(res)
print(len(res))
for r in res:
    print(r)