import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def find(node):
    if parent[node] == -1:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]


def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return

    if x < y:
        parent[py] = px
    else:
        parent[px] = py


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    parent = [-1] * (n + 1)

    for _ in range(m):
        token, a, b = map(int, input().strip().split())
        # union
        if not token:
            union(a, b)
        # find
        else:
            if find(a) != find(b):
                print("NO")
            else:
                print("YES")
