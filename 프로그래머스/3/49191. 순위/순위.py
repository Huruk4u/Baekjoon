from collections import deque


def solution(N, edge):
    answer = 0
    result = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for u, v in edge:
        result[u][v] = 1
        result[v][u] = -1
        
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j or result[i][j] == 1 or result[i][j] == -1:
                    continue
                if result[i][k] == result[k][j] == 1:
                    result[i][j] = 1
                    result[j][i] = -1
    
    for i in range(1, N+1):
        cert = True
        for j in range(1, N+1):
            if i == j: continue
            if not result[i][j]:
                cert = False
                break
                
        if cert:
            answer += 1
            
                
    return answer