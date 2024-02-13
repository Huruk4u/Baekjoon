import sys
input = sys.stdin.readline


def dist(a, b):
    ax, ay = loc[a]
    bx, by = loc[b]
    return ((bx - ax)**2 + (by - ay) ** 2) ** 0.5


def find(curr):
    if parent[curr] == curr:
        return curr
    parent[curr] = find(parent[curr])

    return parent[curr]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

    return True


if __name__ == '__main__':
    N = int(input().strip())

    loc = [tuple(map(float, input().strip().split())) for _ in range(N)]
    edge = []
    for i in range(N):
        for j in range(N):
            edge.append((i, j, dist(i, j)))
    edge.sort(key=lambda x: x[2])
    parent = [i for i in range(N)]

    # solve
    rtn = 0
    for u, v, cost in edge:
        if union(u, v):
            rtn += cost

    print("{:.2f}".format(rtn))
