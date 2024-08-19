import sys
sys.setrecursionlimit(100000001)

def solution(tickets):
    
    rtn = []
    def dfs(curr):
        if len(path) == len(tickets) + 1:
            rtn.append(path[:])
            return
        for next in edge[curr]:
            if not amountTicket[(curr, next)]:
                continue
            path.append(next)
            amountTicket[(curr, next)] -= 1
            dfs(next)
            path.pop()
            amountTicket[(curr, next)] += 1
        return
    
    path = ["ICN"]
    edge = dict()
    amountTicket = dict()
    for u, v in tickets:
        edge[u] = []
        edge[v] = []
    for u, v in tickets:
        edge[u].append(v)
        if (u, v) in amountTicket:
            amountTicket[(u, v)] += 1
        else:
            amountTicket[(u, v)] = 1
    
    
    dfs("ICN")

    rtn.sort()
    return rtn[0]