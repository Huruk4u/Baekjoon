import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(queue):
    while queue:
        curr_y, curr_x, state = queue.popleft()
        for i in range(4):
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]
            # y, x의 유효범위 체크
            if (0 <= next_x < m) and (0 <= next_y < n):
                if visited[next_y][next_x][state]:
                    continue
                tile = matrix[next_y][next_x]
                if tile == '#':
                    continue
                elif 'A' <= tile <= 'F':
                    if state & (1 << (ord(tile) - 65)) == (1 << (ord(tile) - 65)):
                        visited[next_y][next_x][state] = visited[curr_y][curr_x][state] + 1
                        queue.append([next_y, next_x, state])
                    else:
                        continue
                elif 'a' <= tile <= 'f':
                    visited[next_y][next_x][state | (1 << ord(tile) - 97)] = visited[curr_y][curr_x][state] + 1
                    queue.append([next_y, next_x, state | (1 << ord(tile) - 97)])
                elif tile == '1':
                    return visited[curr_y][curr_x][state]
                elif tile == '.' or '0':
                    visited[next_y][next_x][state] = visited[curr_y][curr_x][state] + 1
                    queue.append([next_y, next_x, state])


if __name__ == '__main__':
    # input
    n, m = map(int, input().strip().split())
    matrix = [list(map(str, input().strip())) for _ in range(n)]

    # vst[y][x][state]
    visited = []
    for _ in range(n):
        visited.append([[0] * (1 << 6) for _ in range(m)])

    # starting point
    q = deque()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '0':
                q.append([i, j, 0])
                visited[i][j][0] = 1

    ans = bfs(q)

    if ans is None:
        print(-1)
    else:
        print(ans)