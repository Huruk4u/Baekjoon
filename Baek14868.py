import sys
from collections import deque

input = sys.stdin.readline


def union(a, b):
    civil_a = find(a)
    civil_b = find(b)
    print("%d %d" % (a, b))
    print("%d union %d" % (civil_a, civil_b))
    if civil_a == civil_b:
        return

    civilization[civil_a] = civil_b


def find(node):
    if civilization[node] == node:
        return node
    civilization[node] = find(civilization[node])

    return civilization[node]


# 문명을 합치는 탐색
def combine_civil():
    global k
    while comb_q:
        ci, cj = comb_q.popleft()
        bfs_q.append((ci, cj))
        for t in range(4):
            ni = ci + di[t]
            nj = cj + dj[t]
            # 1. 범위 내에 속하고, 문명이 존재할 것
            if (0 <= ni < n) and (0 <= nj < n) and matrix[ni][nj]:
                # 2. 그 문명이 현재 노드의 문명과 다른 문명일 것
                civil_c = matrix[ci][cj]
                civil_n = matrix[ni][nj]
                if (civil_c == civil_n) or (find(civil_c) == find(civil_n)):
                    continue
                union(civil_c, civil_n)
                print("civilization -> ", civilization)
                k -= 1


def bfs():
    while bfs_q:
        ci, cj = bfs_q.popleft()
        for t in range(4):
            ni = ci + di[t]
            nj = cj + dj[t]
            if (0 <= ni < n) and (0 <= nj < n) and matrix[ni][nj] == 0:
                # 정복되지 않은 지역인 경우.
                matrix[ni][nj] = matrix[ci][cj]
                comb_q.append((ni, nj))


if __name__ == '__main__':
    # n = 세계의 크기, k = 문명 발상지의 수
    n, k = map(int, input().strip().split())

    # matrix[n+1][n+1] = 문명의 정보 c
    matrix = [[0 for _ in range(2001)] for _ in range(2001)]
    # 문명 정보. union-find 때 사용할 parent 정보
    civilization = [i for i in range(k+1)]

    bfs_q = deque()  # bfs에서 사용할 큐
    comb_q = deque()  # combine_civil에서 사용할 큐

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 문명 발원지의 정보를 받으면서 각 matrix에 문명 정보 기입
    for c in range(k):
        i, j = map(int, input().strip().split())
        matrix[i - 1][j - 1] = c + 1
        comb_q.append((i - 1, j - 1))

    for _ in range(n):
        print(matrix[_])

    cnt = 0
    year = 0
    # solve
    while k >= 1:
        combine_civil()
        print(k)
        if k == 1:
            print(year)
            break
        bfs()
        year += 1
        print(year)
