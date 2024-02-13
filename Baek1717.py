import sys

input = sys.stdin.readline


def find(node):
    print("node = %d" % node)
    if parent[node] == -1:
        print("return %d" % node)
        return node
    else:
        return find(parent[node])


def union(x, y):
    print("union")
    px = find(x)
    py = find(y)
    print(px, py)
    if px == py:
        return

    if x < y:
        parent[py] = px
    else:
        parent[px] = py


if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    parent = [-1] * (n + 1)

    for _ in range(n):
        token, a, b = map(int, input().strip().split())
        print("\n================================")
        print("%d %d %d" % (token, a, b))
        # union
        if not token:
            union(a, b)
            print(parent)
        # find
        else:
            if find(a) != find(b):
                print("NO")
            else:
                print("YES")

    print(parent)
