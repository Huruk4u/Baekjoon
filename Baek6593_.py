# 22/09/15
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs(curr_x, curr_y, curr_h):
    global dx, dy, dh, height, total_x, total_y
    queue = deque(([0, 0, 0], [curr_h, curr_y, curr_x]))
    visited[curr_h][curr_y][curr_x] = 1
    queue.popleft()
    while queue:
        current_pos = queue.popleft()
        curr_h = current_pos[0]
        curr_y = current_pos[1]
        curr_x = current_pos[-1]

        for i in range(6):
            next_h = curr_h + dh[i]
            next_y = curr_y + dy[i]
            next_x = curr_x + dx[i]
            if (0 <= next_h < height) and (0 <= next_y < total_y) and (0 <= next_x < total_x):
                if not visited[next_h][next_y][next_x]:
                    if building[next_h][next_y][next_x] == '.':
                        queue.append([next_h, next_y, next_x])
                        visited[next_h][next_y][next_x] = visited[curr_h][curr_y][curr_x] + 1
                    elif building[next_h][next_y][next_x] == 'E':
                        return visited[curr_h][curr_y][curr_x]


while True:
    height, total_y, total_x = map(int, input().strip().split())
    if height == total_y == total_x == 0:
        break

    building = []
    visited = []
    for _ in range(height):
        building.append([list(input().strip()) for _ in range(total_y)])
        visited.append([[0]*total_x for _ in range(total_y)])
        input()

    # check start point
    start_h = 0
    start_y = 0
    start_x = 0
    for h in range(height):
        for y in range(total_y):
            for x in range(total_x):
                if building[h][y][x] == 'S':
                    start_h = h
                    start_y = y
                    start_x = x
                    break

    # main
    res = bfs(start_x, start_y, start_h)
    if res is None:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)."%(res))
