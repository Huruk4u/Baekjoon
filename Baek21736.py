import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def in_range(x, y):
    if (0 <= x < N) and (0 <= y < M):
        return True
    else:
        return False


def dfs(cx, cy):
    global cnt
    visited[cx][cy] = True
    if matrix[cx][cy] == 'P':
        cnt += 1
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if in_range(nx, ny) and not visited[nx][ny]:
            if matrix[nx][ny] == 'X':
                continue
            dfs(nx, ny)

    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(input().strip()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'I':
                si, sj = i, j

    cnt = 0
    dfs(si, sj)
    if not cnt:
        print("TT")
    else:
        print(cnt)
