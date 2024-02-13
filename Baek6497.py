import sys
input = sys.stdin.readline
INF = sys.maxsize


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
    while True:
        N, M = map(int, input().strip().split())
        if N == 0 and M == 0:
            break

        edge = []
        for _ in range(M):
            a, b, c = map(int, input().strip().split())
            edge.append((a, b, c))
        edge.sort(key=lambda x: x[2])

        parent = [i for i in range(N)]
        rtn = 0
        for u, v, cost in edge:
            if union(u, v):
                continue
            else:
                rtn += cost

        print(rtn)
