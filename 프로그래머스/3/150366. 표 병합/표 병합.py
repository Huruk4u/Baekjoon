import sys
from collections import defaultdict
sys.setrecursionlimit(100000001)


parent = dict()
value = defaultdict(str)
# union-find 사용할 듯
for i in range(1, 51):
    for j in range(1, 51):
        parent[(i, j)] = (i, j)


def find(node):
    if parent[node] == node:
        return parent[node]
    parent[node] = find(parent[node])
    return parent[node]


def merge(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return
    else:
        if value[root2] and not value[root1]:
            parent[root1] = root2
        else:
            parent[root2] = root1
        return
    
    
def unmerge(node):
    root = find(node)
    value[node] = value[root]
    backup = []
    # 문제의 그 코드
    for i in range(1, 51):
        for j in range(1, 51):
            if find((i, j)) == root:
                backup.append((i, j))                
    
    for vert in backup:
        parent[vert] = vert
        if vert == node:
            continue
        value[vert] = ""
        
    return


def solution(commands):
    answer = []
    
    for command in commands:
        command = list(command.split())
        if command[0] == "UPDATE":
            if len(command) == 4:   # UPDATE RC VALUE:
                r, c = int(command[1]), int(command[2])
                value[find((r, c))] = command[3]
            else: # UPDATE VALUE1 TO VALUE2
                value1, value2 = command[1], command[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if value[find((i, j))] == value1:
                            value[find((i, j))] = value2
                
        elif command[0] == "MERGE":
            node1, node2 = (int(command[1]), int(command[2])), (int(command[3]), int(command[4]))
            merge(node1, node2)
            
        elif command[0] == "UNMERGE":
            node = (int(command[1]), int(command[2]))
            unmerge(node)
            
        else:   # command[0] == "PRINT"
            node = (int(command[1]), int(command[2]))
            rtn = "EMPTY" if not value[find(node)] else value[find(node)]
            answer.append(rtn)
    
    return answer