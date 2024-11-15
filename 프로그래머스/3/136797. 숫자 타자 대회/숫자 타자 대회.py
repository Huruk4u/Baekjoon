import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000001)
INF = sys.maxsize

# 수평 이동, 대각 이동
cdy, cdx = [-1, 1, 0, 0], [0, 0, -1, 1]
xdy, xdx = [-1, -1, 1, 1], [-1, 1, 1, -1]


def in_range(y, x):
    if (0 <= x < 3) and (0 <= y < 4):
        return True
    else:
        return False


def bfs(queue):
    visited = [[INF, INF, INF] for _ in range(4)]
    visited[queue[0][0]][queue[0][1]] = 0
    while queue:
        cy, cx = queue.popleft()
        # 수평 이동
        for i in range(4):
            ny, nx = cy + cdy[i], cx + cdx[i]
            new_dist = visited[cy][cx] + 2
            if not in_range(ny, nx) or visited[ny][nx] <= new_dist:
                continue
            visited[ny][nx] = new_dist
            queue.append((ny, nx))

        for i in range(4):
            ny, nx = cy + xdy[i], cx + xdx[i]
            new_dist = visited[cy][cx] + 3
            if not in_range(ny, nx) or visited[ny][nx] <= new_dist:
                continue
            visited[ny][nx] = new_dist
            queue.append((ny, nx))

    return visited


def solution(numbers):
    pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    dist = dict()  # 문자열 u - v간 최소거리를 저장한 dict
    for i in range(4):
        for j in range(3):
            rtn = bfs(deque([(i, j)]))
            rtn[i][j] = 1

            min_dist = dict()
            for y in range(4):
                for x in range(3):
                    min_dist[pad[y][x]] = rtn[y][x]

            dist[pad[i][j]] = min_dist

    cost = defaultdict(lambda: INF)
    cost[('4', '6', 0)] = 0
    queue = deque([('4', '6', 0)])
    while queue:
        left, right, idx = queue.popleft()
        if idx >= len(numbers):
            continue

        num = numbers[idx]

        if num != right:
            new_cost = cost[(left, right, idx)] + dist[left][num]
            if new_cost < cost[(num, right, idx+1)]:
                cost[(num, right, idx+1)] = new_cost
                queue.append((num, right, idx+1))

        if num != left:
            new_cost = cost[(left, right, idx)] + dist[num][right]
            if new_cost < cost[(left, num, idx+1)]:
                cost[(left, num, idx+1)] = new_cost
                queue.append((left, num, idx+1))

    answer = INF
    for key, value in cost.items():
        if key[2] == len(numbers):
            answer = min(answer, value)

    return answer