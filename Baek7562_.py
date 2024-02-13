# 22/09/12
import sys
from collections import deque

sys.setrecursionlimit(10001)

testCase = int(input().strip())
input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, 2, 1, 1, 2, -2, -1]


def bfs(current_x, current_y, final_x, final_y):
    path = deque()
    path.append((current_x, current_y))
    while path:
        current_x, current_y = path.popleft()
        if current_x == final_x and current_y == final_y:
            print(visited[current_x][current_y]-1)
            return
        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            if (0 <= next_x < n) and (0 <= next_y < n):
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = visited[current_x][current_y] + 1
                    path.append((next_x, next_y))


if __name__ == '__main__':
    for _ in range(testCase):
        n = int(input().strip())
        x, y = map(int,input().strip().split())
        final_x, final_y = map(int,input().strip().split())

        visited = [[0]*n for _ in range(n)]
        visited[x][y] = 1
        bfs(x, y, final_x, final_y)