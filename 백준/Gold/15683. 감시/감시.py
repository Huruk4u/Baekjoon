import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(y, x):
    return (0 <= y < N) and (0 <= x < M)


def backtracking(depth):
    global answer

    if depth == len(cctvs):
        temp = 0
        for y in range(N):
            for x in range(M):
                if not matrix[y][x]: temp += 1
        answer = min(answer, temp)
        return

    cy, cx, type = cctvs[depth]
    vision = [] # (dy, dx)
    if type == 1:
        vision = deque([1, 0, 0, 0])
    elif type == 2:
        vision = deque([1, 0, 1, 0])
    elif type == 3:
        vision = deque([1, 1, 0, 0])
    elif type == 4:
        vision = deque([1, 1, 1, 0])
    else:
        vision = deque([1, 1, 1, 1])

    for r in range(4): # 시야 회전
        for i in range(4): # 감시 구역 칠하기
            if not vision[i]: continue

            delta = 1
            while True:
                ny = cy + (dy[i] * delta)
                nx = cx + (dx[i] * delta)
                if not in_range(ny, nx) or matrix[ny][nx] == 6:
                    break
                delta += 1
                if 0 < matrix[ny][nx] < 6: continue
                matrix[ny][nx] -= 1

        backtracking(depth + 1)

        for i in range(4): # 감시 구역 지우기
            if not vision[i]: continue

            delta = 1
            while True:
                ny = cy + (dy[i] * delta)
                nx = cx + (dx[i] * delta)
                if not in_range(ny, nx) or matrix[ny][nx] == 6:
                    break
                delta += 1
                if 0 < matrix[ny][nx] < 6: continue
                matrix[ny][nx] += 1

        vision.rotate()

    return



if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    cctvs = [] # (y, x, cctv_type)
    for y in range(N):
        for x in range(M):
            if 0 < matrix[y][x] < 6:
                cctvs.append((y, x, matrix[y][x]))

    answer = INF
    backtracking(0)
    print(answer)
