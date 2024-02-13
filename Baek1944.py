import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_locate():
    node_rtn = []
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 'S' or miro[i][j] == 'K':
                node_rtn.append((i, j))
    return node_rtn


def bfs(y, x):
    queue = deque([(y, x)])
    start = (y, x)
    vst[y][x] = 1
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < N) and (0 <= nx < N) and not vst[ny][nx]:
                if miro[ny][nx] == 'K' or miro[ny][nx] == 'S':
                    edge.append((to_number[start], to_number[(ny, nx)], vst[cy][cx]))
                    vst[ny][nx] = vst[cy][cx] + 1
                elif miro[ny][nx] == '0':
                    queue.append((ny, nx))
                    vst[ny][nx] = vst[cy][cx] + 1
                else:
                    continue


def find(curr):
    if parent[curr] == curr:
        return curr
    parent[curr] = find(parent[curr])
    return parent[curr]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return True


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    miro = [list(input().strip()) for _ in range(N)]

    node = get_locate()
    to_number = dict()  # locate --> node Number
    for i in range(M+1):
        to_number[node[i]] = i

    # 엣지 추출
    edge = []
    for si, sj in node:
        vst = [[0] * N for _ in range(N)]
        bfs(si, sj)

    edge.sort(key=lambda x: x[2])
    parent = [i for i in range(M+1)]

    rtn = 0
    key_cnt = 0
    for u, v, cost in edge:
        if union(u, v):
            rtn += cost
            key_cnt += 1

    if key_cnt < M:
        print(-1)
    else:
        print(rtn)
