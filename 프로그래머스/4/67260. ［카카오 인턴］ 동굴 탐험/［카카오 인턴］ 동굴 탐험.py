from collections import deque


def solution(N, path, order):
    answer = True
    
    def bfs(curr):
        queue = deque([curr])
        visited[curr] = True
        visited_cnt = 0
        while queue:
            curr = queue.popleft()
            
            if lock[curr] and not visited[lock[curr]]:
                non_find[lock[curr]] = curr
                continue
                
            visited[curr] = True
            visited_cnt += 1
            
            for next in graph[curr]:
                if visited[next]: continue
                queue.append(next)
            if curr in non_find:
                queue.append(non_find[curr])
                
        return visited_cnt
    
    graph = [[] for _ in range(N)]
    for u, v in path:
        graph[u].append(v)
        graph[v].append(u)
    
    non_find, lock = dict(), [0] * N
    for u, v in order:
        lock[v] = u
    
    visited = [False] * N
    visited_cnt = bfs(0)
    
    if visited_cnt == N:
        return True
    else:
        return False
