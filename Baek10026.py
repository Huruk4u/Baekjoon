# 22/09/05
import sys
sys.setrecursionlimit(10001)

n = int(sys.stdin.readline().strip())

matrix = []
for _ in range(n):
    a = list(sys.stdin.readline().strip())
    matrix.append(a)
is_visit = [[False]*n for _ in range(n)]

def normal(x,y):
    is_visit[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if (0 <= _x < n) and (0 <= _y < n) :
            if not is_visit[_x][_y]:
                if matrix[x][y] == matrix[_x][_y]:
                    normal(_x,_y)

def blind(x,y):
    is_visit[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]
        if (0 <= _x < n) and (0 <= _y < n) :
            if not is_visit[_x][_y]:
                if matrix[x][y] == 'R' or matrix[x][y] == 'G':
                    if matrix[_x][_y] != 'B':
                        blind(_x,_y)
                else :
                    if matrix[_x][_y] == 'B':
                        blind(_x,_y)

component = 0
res_normal = 0
res_blind = 0

for x in range(n):
    for y in range(n):
        if not is_visit[x][y]:
            component += 1
            normal(x,y)
res_normal = component

is_visit = [[False]*n for _ in range(n)]
component = 0

for x in range(n):
    for y in range(n):
        if not is_visit[x][y]:
            component += 1
            blind(x,y)
res_blind = component

print(res_normal,res_blind)