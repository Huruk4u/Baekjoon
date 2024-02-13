# 22/08/31
import sys
sys.setrecursionlimit(10001)
n,m = map(int,sys.stdin.readline().strip().split())

isVisit = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,sys.stdin.readline().strip().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(start):
    isVisit[start] = True
    for i in graph[start]:
        if not isVisit[i]:
            dfs(i)

component = 0
for i in range(1,n+1):
    if not isVisit[i]:
        if not graph[i]:
            component += 1
            isVisit[i] = True
        else:
            component += 1
            dfs(i)

print(component)