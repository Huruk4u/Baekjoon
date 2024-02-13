import sys
from collections import deque


def bfs(queue):
    while queue:
        curr, zero, cnt = queue.popleft()
        if curr == sorted_puz:
            return cnt



    return -1


if __name__ == '__main__':
    # input
    puzzle = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]
    sorted_puz = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # 2차원 -> 1차원
    puz = []
    for i in range(3):
        for j in range(3):
            puz.append(puzzle[i][j])

    # 0
    idx_zero = 0
    for i in range(9):
        if puz[i] == 0:
            idx_zero = i
    # queue[현재 퍼즐 상태, 0의 위치, cnt]
    q = deque()
    q.append([puz, idx_zero, 0])