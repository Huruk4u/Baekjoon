import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def to_string(puz):
    rtn = ''
    for y in range(3):
        for x in range(3):
            rtn += puz[y][x]
    return rtn


def switch(loc1, loc2, puz):
    new_puz = [puz[i][:] for i in range(3)]
    y1, x1 = loc1
    y2, x2 = loc2
    new_puz[y1][x1], new_puz[y2][x2] = new_puz[y2][x2], new_puz[y1][x1]
    return new_puz


def bfs(queue):
    curr, loc_0, cnt = queue[0]
    vst.add(to_string(curr))
    while queue:
        curr, loc_0, cnt = queue.popleft()
        if curr == sorted_puz:
            return cnt
        for i in range(4):
            ny = loc_0[0] + dy[i]
            nx = loc_0[1] + dx[i]
            if (0 <= nx < 3) and (0 <= ny < 3):
                next_puz = switch(loc_0, (ny, nx), curr)
                next_str = to_string(next_puz)
                if next_str not in vst:
                    vst.add(next_str)
                    queue.append([next_puz, (ny, nx), cnt+1])
    return -1


if __name__ == '__main__':
    # input
    puzzle = [list(map(str, sys.stdin.readline().strip().split())) for _ in range(3)]
    sorted_puz = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

    # queue[퍼즐의 현재 상태, 0의 위치, cnt]
    q = deque()
    idx_0 = tuple()
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                idx_0 = (i, j)

    q.append([puzzle, idx_0, 0])

    # visited
    vst = set()

    print(bfs(q))