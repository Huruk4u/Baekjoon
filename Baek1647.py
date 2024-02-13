import sys
input = sys.stdin.readline


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
    N, M = map(int, input().strip().split())
    edge = []
    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        edge.append((a, b, c))
    edge.sort(key=lambda x: x[2])

    parent = [i for i in range(N + 1)]
    last_cost = 0
    rtn = 0
    for u, v, cost in edge:
        if union(u, v):
            rtn += cost
            last_cost = cost

    print(rtn - last_cost)
    