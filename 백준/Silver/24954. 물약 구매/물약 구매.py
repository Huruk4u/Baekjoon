import sys
from copy import deepcopy
input = sys.stdin.readline
INF = sys.maxsize


def solve(curr, cnt, spend):
    global rtn

    if cost[curr] - sale_cost[curr] > 0:
        spend += cost[curr] - sale_cost[curr]
    else:
        spend += 1

    cnt += 1

    if cnt == N:
        rtn = min(rtn, spend)
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        for _ in range(len(sale[curr])):
            number, c = sale[curr][_]
            sale_cost[number] += c
        solve(i, cnt, spend)
        visited[i] = False
        for _ in range(len(sale[curr])):
            number, c = sale[curr][_]
            sale_cost[number] -= c
    return


if __name__ == '__main__':
    N = int(input().strip())
    cost = list(map(int, input().strip().split()))
    sale = [[] for _ in range(N)]
    for i in range(N):
        sale_n = int(input().strip())
        for _ in range(sale_n):
            n, price = map(int, input().strip().split())
            sale[i].append((n-1, price))

    rtn = INF
    visited = [False] * N
    sale_cost = [0] * N
    for i in range(N):
        visited[i] = True
        solve(i, 0, 0)
        visited[i] = False

    print(rtn)
