import sys
sys.setrecursionlimit(10000001)
input = sys.stdin.readline


def dfs(curr):
    global get_team

    visited[curr] = True
    path.append(curr)

    if visited[graph[curr]]:
        if graph[curr] in path:
            get_team += len(path[path.index(graph[curr]):])
            return
        else:
            return
    dfs(graph[curr])



if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        graph = [0] + list(map(int, input().strip().split()))
        get_team = 0

        visited = [False] * (N+1)
        for i in range(1, N+1):
            if visited[i]: continue
            path = []
            dfs(i)

        print(N - get_team)

