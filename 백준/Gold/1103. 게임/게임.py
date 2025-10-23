import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000001)

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


def dfs(cy, cx):
    if visited[cy][cx]: return -1

    if dp[cy][cx]:
        return dp[cy][cx]

    visited[cy][cx] = True
    dp[cy][cx] = 0

    for i in range(4):
        ny = cy + dy[i] * int(matrix[cy][cx])
        nx = cx + dx[i] * int(matrix[cy][cx])

        if not in_range(ny, nx) or matrix[ny][nx] == 'H': continue

        rtn = dfs(ny, nx)
        if rtn == -1:
            dp[cy][cx] = -1
            visited[cy][cx] = False
            return -1

        dp[cy][cx] = max(dp[cy][cx], rtn + 1)

    visited[cy][cx] = False

    return dp[cy][cx]


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(input().strip()) for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    answer = dfs(0, 0)
    print(answer + 1 if answer != -1 else -1)
