# 22/09/20
import sys
from collections import deque

x, y = map(int, sys.stdin.readline().strip().split())
tomato = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(y)]
conquer = True

queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 익은 토마토가 애초에 있지 않은 경우 고려 x
def bfs(t_queue):
    cnt = 0
    while t_queue:
        print("=========================\n cnt -> %d" % (cnt))
        for _ in range(len(t_queue)):
            curr_y, curr_x = t_queue.popleft()
            for i in range(4):
                next_x = curr_x + dx[i]
                next_y = curr_y + dy[i]
                if (0 <= next_x < x) and (0 <= next_y < y):
                    if tomato[next_y][next_x] == 0:
                        print("visited %d %d" % (next_y, next_x))
                        tomato[next_y][next_x] = 1
                        t_queue.append((next_y, next_x))
        cnt += 1
        print(tomato)
    return cnt


if __name__ == '__main__':
    for i in range(y):
        for j in range(x):
            if tomato[i][j] == 1:
                queue.append((i, j))

    res = bfs(queue)

    for i in range(y):
        for j in range(x):
            if tomato[i][j] == 0:
                conquer = False

    if conquer:
        print(res - 1)
    else:
        print(-1)