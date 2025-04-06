from collections import deque
from pprint import pprint

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x, N, M):
    return (0 <= y < N) and (0 <= x < M)


def bfs(queue, matrix, visited):
    N, M = len(matrix), len(matrix[0])
    visited[0][0] = 1
    while queue:
        cy, cx = queue.popleft()
        
        if cy == N-1 and cx == M-1:
            return visited[cy][cx]
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx, N, M) or visited[ny][nx]:
                continue
            if not matrix[ny][nx]: continue    
            visited[ny][nx] = visited[cy][cx] + 1
            queue.append((ny, nx))
    
    return -1
    

def solution(maps):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = bfs(deque([(0, 0)]), maps, visited)
    
    pprint(visited)
    
    return answer