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
    if root_x <= root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

    return True


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())

    edge = []
    parent = [i for i in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().strip().split())
        edge.append((a, b, c))
    edge.sort(key=lambda x: x[2])

    rtn = 0
    for u, v, c in edge:
        print("------------------------------------------------------")
        print("%d - %d : %d" % (u, v, c))

        if union(u, v):
            print("%d union %d" % (u, v))
            rtn += c

    print(parent)
    print(rtn)
