# 22/09/11
import sys
from collections import deque

sys.setrecursionlimit(10001)

n,m = map(int,sys.stdin.readline().strip().split())
matrix = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i,j):
    path = deque()
    path.append([i, j])
    while path:
        i, j = path.popleft()
        for k in range(4):
            next_i = i+di[k]
            next_j = j+dj[k]
            if (0 <= next_i < n) and (0 <= next_j < m):
                if matrix[next_i][next_j] and matrix[next_i][next_j] == 1:
                    matrix[next_i][next_j] = matrix[i][j] + 1
                    path.append([next_i, next_j])
    return matrix[n-1][m-1]


print(bfs(0, 0))