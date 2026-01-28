import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

dcy = [-1, 1, 0, 0]
dcx = [0, 0, -1, 1]

dd = [[(-1, -1), (-1, 1)], [(1, -1), (1, 1)], [(-1, -1), (1, -1)], [(-1, 1), (1, 1)]]

def in_range(y, x):
    return (0 <= y < 10 and 0 <= x < 9)

def enemy_bloced(y, x):
    return y == ey and x == ex

def bfs(queue):
    visited[queue[0][0]][queue[0][1]] = 1
    while queue:
        cy, cx = queue.popleft()
        if cy == ey and cx == ex:
            return visited[cy][cx] - 1

        for i in range(4):
            ncy = cy + dcy[i]
            ncx = cx + dcx[i]
            if not in_range(ncy, ncx) or enemy_bloced(ncy, ncx):
                continue

            for delta_diag in dd[i]:
                ddy, ddx = delta_diag
                for k in range(1, 3):
                    ndy = ncy + ddy * k
                    ndx = ncx + ddx * k
                    if k == 1:
                        if not in_range(ndy, ndx) or enemy_bloced(ndy, ndx): break
                    else:
                        if not in_range(ndy, ndx) or visited[ndy][ndx] != 0: continue
                        visited[ndy][ndx] = visited[cy][cx] + 1
                        queue.append((ndy, ndx))

    return -1


if __name__ == '__main__':
    sy, sx = map(int, input().strip().split())
    ey, ex = map(int, input().strip().split())

    queue = deque()
    queue.append((sy, sx))

    visited = [[0] * 9 for _ in range(10)]

    print(bfs(queue))
