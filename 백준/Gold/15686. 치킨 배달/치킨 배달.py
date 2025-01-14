import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def backtracking(curr, depth):
    global answer

    if depth == M:
        new_answer = 0
        for hy, hx in house:
            dist = sys.maxsize
            for i in range(len(chicken)):
                if not visited[i]: continue
                dist = min(dist, abs(chicken[i][0] - hy) + abs(chicken[i][1] - hx))
            new_answer += dist
        answer = min(answer, new_answer)
        return

    for next in range(curr, len(chicken)):
        if visited[next]: continue
        visited[next] = True
        backtracking(next, depth + 1)
        visited[next] = False
    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    house, chicken = [], []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                house.append((i, j))
            elif matrix[i][j] == 2:
                chicken.append((i, j))

    answer = sys.maxsize
    visited = [False] * len(chicken)
    backtracking(0, 0)

    print(answer)
