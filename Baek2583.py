# 22/09/05
import sys
sys.setrecursionlimit(10001)
m,n,k = map(int,sys.stdin.readline().strip().split())

def dfs(x,y):
    global depth
    is_visit[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        _x = x+dx[i]
        _y = y+dy[i]
        if (0 <= _x < m) and (0 <= _y < n) :
            if not is_visit[_x][_y] and matrix[_x][_y]:
                depth += 1
                dfs(_x,_y)

matrix = [[True]*n for _ in range(m)]
is_visit = [[False]*n for _ in range(m)]
component = 0
res = []
for _ in range(k):
    a,b,x,y = map(int,sys.stdin.readline().strip().split())
    for v in range(b,y):
        for h in range(a,x):
            if matrix[v][h] :
               matrix[v][h] = False

for x in range(m):
    for y in range(n):
        if not is_visit[x][y] and matrix[x][y]:
            depth = 1
            component += 1
            dfs(x,y)
            res.append(depth)
res = sorted(res)

print(component)
for r in res:
    print("%d"%(r),end=" ")