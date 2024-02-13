# 22/09/16
import sys
from collections import deque

T = int(sys.stdin.readline().strip())

dx = [-1, 1, 0, 0]
dh = [0, 0, -1, 1]


def bfs(queue, fire, cnt):
    global visited, dx, dh
    while queue:
        cnt += 1
        for _ in range(len(fire)):
            fire_h, fire_x = fire.popleft()
            for i in range(4):
                fire_nh = fire_h + dh[i]
                fire_nx = fire_x + dx[i]
                if (0 <= fire_nx < width) and (0 <= fire_nh < height):
                    if building[fire_nh][fire_nx] == '.':
                        building[fire_nh][fire_nx] = '*'
                        fire.append((fire_nh, fire_nx))
        print("building ==\n", building)

        for _ in range(len(queue)):
            curr_h, curr_x = curr.popleft()
            print("queue -> ", queue)

            for i in range(4):
                next_h = curr_h + dh[i]
                next_x = curr_x + dx[i]
                if (0 <= next_x < width) and (0 <= next_h < height):
                    if building[next_h][next_x] == '.' and not visited[next_h][next_x]:
                        # escape
                        if (next_x == 0 or next_x == width-1) or (next_h == 0 or next_h == height-1):
                            return visited[curr_h][curr_x] + 1
                        print("visited %d %d" % (next_h, next_x))
                        visited[next_h][next_x] = visited[curr_h][curr_x] + 1
                        queue.append((next_h, next_x))


for _ in range(T):
    print("================================")
    width, height = map(int, sys.stdin.readline().strip().split())
    building = [list(sys.stdin.readline().strip()) for k in range(height)]
    visited = [[0] * width for a in range(height)]

    fire = deque()
    curr = deque()
    # brute force
    for y in range(height):
        for x in range(width):
            if building[y][x] == '@':
                curr.append((y, x))
                visited[y][x] = 1
            elif building[y][x] == '*':
                fire.append((y, x))

    res = bfs(curr, fire, 0)

    if res is None:
        print("IMPOSSIBLE")
    else:
        print(res)
