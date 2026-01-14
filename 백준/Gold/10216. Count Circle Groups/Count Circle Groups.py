import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def get_distance(u, v):
    return (nodes[u][0] - nodes[v][0]) ** 2 + (nodes[u][1] - nodes[v][1]) ** 2

def dfs(curr):
    visited[curr] = True
    for next in graph[curr]:
        if visited[next]: continue
        dfs(next)

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        nodes = []
        for i in range(N):
            y, x, r = map(int, input().strip().split())
            nodes.append((y, x, r))

        graph = [[] for dum in range(N)]
        for u in range(N):
            for v in range(u+1, N):
                if u == v: continue
                if get_distance(u, v) <= (nodes[u][2] + nodes[v][2]) ** 2:
                    graph[u].append(v)
                    graph[v].append(u)

        visited = [False for dum in range(N)]
        answer = 0
        for u in range(N):
            if visited[u]: continue
            dfs(u)
            answer += 1

        print(answer)
