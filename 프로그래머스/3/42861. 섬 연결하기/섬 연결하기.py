import heapq

def solution(n, edges):
    
    def find(node):
        if parent[node] == node:
            return node
        parent[node] = find(parent[node])
        return parent[node]
    
    def union(x, y, cost):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return 0
        else:
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
            return cost
    
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]    
    answer = 0
    for u, v, cost in edges:
        answer += union(u, v, cost)
    
    return answer