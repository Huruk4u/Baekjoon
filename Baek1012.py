# 22/08/31
import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline
T = int(input().strip())

def dfs(x,y):
    is_visit[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        _x = x+dx[i]
        _y = y+dy[i]
        if (0 <= _x < m) and (0 <= _y < n):
            print(graph[_x][_y],_x,_y)
            if graph[_x][_y]:
                if not is_visit[_x][_y]:
                    print("visit %d %d"%(_x,_y))
                    dfs(_x,_y)

for _ in range(T):
    m,n,k = map(int,input().strip().split())
    graph = [[False]*n for a in range(m)]
    vertex = []
    is_visit = [[False]*n for a in range(m)]

    for b in range(k):
        x,y = map(int,input().strip().split())
        graph[x][y]=True
        vertex.append([x,y])
    component = 0
    for x,y in vertex:
        print("=====================\n%d %d"%(x,y))
        if not is_visit[x][y]:
            print("반응함")
            dfs(x,y)
            component+=1
        print("graph is",graph)
        print("is_visit is",is_visit)
    print(component)
