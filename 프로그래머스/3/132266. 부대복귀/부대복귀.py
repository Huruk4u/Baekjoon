from collections import deque


def solution(N, roads, sources, destination):
    
    def bfs(queue):
        while queue:
            curr = queue.popleft()
            for next in graph[curr]:
                if visited[next]: continue
                visited[next] = visited[curr] + 1
                queue.append(next)
        
        return
    
    graph = [[] for _ in range(N+1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    visited, result = [0 for _ in range(N+1)], []
    visited[destination] = 1
    bfs(deque([destination]))
    for start in sources:
        result.append(visited[start] - 1)
        
    
    return result