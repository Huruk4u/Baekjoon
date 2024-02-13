# 22/09/14
import sys
from collections import deque

total_f, start_f, end_f, up, down = map(int,sys.stdin.readline().strip().split())
visited = [0] * (total_f+1)
move = [up,-down]


def bfs(current_f, end):
    global total_f, move, visited
    queue = deque([current_f])
    visited[current_f] = 1
    while queue:
        current_f = queue.popleft()
        if current_f == end:
            return visited[current_f] - 1

        for m in move:
            next_floor = current_f + m
            if 0 < next_floor <= total_f and not visited[next_floor]:
                visited[next_floor] = visited[current_f] + 1
                queue.append(next_floor)


if __name__ == '__main__':
    res = bfs(start_f, end_f)
    if res is None:
        print("use the stairs")
    else:
        print(res)