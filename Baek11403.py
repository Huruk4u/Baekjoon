import sys
sys.setrecursionlimit(30001)
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]

def dfs(vst, start, now):
    for nxt in range(N):
        if graph[now][nxt] == 1 and nxt not in vst:
            vst.add(nxt)
            ans[start][nxt] = 1
            dfs(vst, start, nxt)

if __name__ == '__main__':
    for x in range(N):
        dfs(set(), x, x)

    for line in range(N):
        print(*ans[line])
