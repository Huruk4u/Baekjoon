# 22/09/05
import sys
sys.setrecursionlimit(10001)

def dfs(i, start):
    for j in range(n):
        if matrix[i][j] == 1 and ans[start][j] == 0:
            ans[start][j] = 1
            dfs(j,start)

n = int(sys.stdin.readline().strip())
matrix = []
for _ in range(n):
    a = list(map(int,sys.stdin.readline().strip().split()))
    matrix.append(a)
ans = [[0]*n for _ in range(n)]

for i in range(n):
    dfs(i,i)

for a in range(n):
    print(' '.join(map(str, ans[a])))
