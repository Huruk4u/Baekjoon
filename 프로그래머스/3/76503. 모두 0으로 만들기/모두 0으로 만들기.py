from collections import deque
from copy import deepcopy

def solution(a, edges):
    
    answer = -2
    
    # 배열 a의 합이 0이 아니면 모든 점들의 가중치가 0이 되지 않으므로 return
    if sum(a) != 0:
        return -1
    
    graph = [[] for _ in range(len(a))]
    inDeg = [0 for _ in range(len(a))]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        inDeg[u] += 1
        inDeg[v] += 1
    
    queue = deque()
    for i in range(len(a)):
        if inDeg[i] == 1:
            queue.append(i)
    
    answer = 0
    cnt = [0 for _ in range(len(a))]
    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            inDeg[next] -= 1
            if inDeg[next] == 1:
                queue.append(next)
            if a[next]:
                cnt[next] += cnt[curr] + abs(a[curr])
                a[next] += a[curr]
                a[curr] = 0
                
    return max(cnt)