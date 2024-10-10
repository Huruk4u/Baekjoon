from collections import deque


def solution(N, edges):
    
    def bfs(queue):
        vst = [-1] * (N+1)
        vst[queue[0]] = 0
        while queue:
            curr = queue.popleft()
            for next in graph[curr]:
                if vst[next] != -1: continue
                queue.append(next)
                vst[next] = vst[curr] + 1
                
        return vst
    
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    root, root_deg = 0, 0
    for i in range(len(graph)):
        if len(graph[i]) > root_deg:
            root_deg = len(graph[i])
            root = i
            
    dist = bfs(deque([root]))
    leaf = dist.index(max(dist))
    
    dist = bfs(deque([leaf]))
    leaf = dist.index(max(dist))
    dist.sort(reverse = True)
    if dist[0] == dist[1]:
        return dist[0]
    else:
        dist = sorted(bfs(deque([leaf])), reverse=True)
        answer = dist[1]
        return answer