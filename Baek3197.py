import sys
from collections import deque
input = sys.stdin.readline


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def in_range(ni, nj):
    if (0 <= ni < r) and (0 <= nj < c):
        return True
    else:
        return False


def to_water():
    print("to_water")
    while boundary_q:
        ci, cj, flag = boundary_q.popleft()
        if flag:
            lake[ci][cj] = flag
            swan_q.append((ci, cj))
        else:
            lake[ci][cj] = 0
            water_q.append((ci, cj))


def to_boundary():
    while water_q:
        ci, cj = water_q.popleft()
        print("to_boundary")
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if not in_range(ni, nj):
                continue
            if lake[ni][nj] == 3:
                if visited[ni][nj]:
                    continue
                boundary_q.append((ni, nj, 0))
                visited[ni][nj] = True


def swan():
    print("swan")
    global union
    while swan_q:
        ci, cj = swan_q.popleft()
        c_swan = lake[ci][cj]
        print("-------------------------")
        print("%d %d %d" % (ci, cj, c_swan))
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if not in_range(ni, nj):
                continue
            print("%d %d %d" % (ni, nj, lake[ni][nj]))
            if lake[ni][nj] == 3:
                if visited[ni][nj]:
                    continue
                boundary_q.append((ni, nj, c_swan))
                visited[ni][nj] = True
            elif lake[ni][nj] == 0:
                lake[ni][nj] = c_swan
                swan_q.append((ni, nj))
                visited[ni][nj] = True
            elif lake[ni][nj] != c_swan:
                union = True
                break


if __name__ == '__main__':
    r, c = map(int, input().strip().split())
    ipt = [list(map(str, input().strip())) for _ in range(r)]
    lake = [[3 for _ in range(c)] for _ in range(r)]

    boundary_q = deque()
    swan_q = deque()
    water_q = deque()
    visited = [[False] * c for _ in range(r)]

    swan_n = 1
    for i in range(r):
        for j in range(c):
            s = ipt[i][j]
            if s == '.':
                lake[i][j] = 0
            elif s == 'L':
                lake[i][j] = swan_n
                swan_n += 1
                swan_q.append((i, j))

    union = False
    day = 0

    swan()
    for i in range(r):
        for j in range(c):
            if lake[i][j] == 0:
                water_q.append((i, j))
    if union:
        print(day)
    else:
        while True:
            day += 1
            to_boundary()
            to_water()
            swan()
            if union:
                print(day)
                break
            for _ in range(r):
                print(lake[_])
            print("boundary_q", boundary_q)
            print("water_q", water_q)
            print("swan_q", swan_q)
