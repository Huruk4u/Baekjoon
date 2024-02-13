import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000001)


def find(node):
    if parent[node] == node:
        return node

    parent[node] = find(parent[node])

    return parent[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return

    if cost[root_x] < cost[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


if __name__ == '__main__':
    # input
    n, m, k = map(int, input().strip().split())
    cost = [0] + list(map(int, input().strip().split()))

    parent = [i for i in range(n + 1)]
    # union
    for _ in range(m):
        a, b = map(int, input().strip().split())
        union(a, b)

    # calculate
    visited = [False] * (n + 1)
    total = 0

    for i in range(1, n+1):
        root_i = find(i)
        if not visited[root_i]:
            visited[root_i] = True
            total += cost[root_i]

    # print
    if total > k:
        print("Oh no")
    else:
        print(total)
