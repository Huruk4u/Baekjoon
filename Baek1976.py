import sys

input = sys.stdin.readline


def find(node):
    if not parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    print("root_a = %d, root_b = %d" % (root_a, root_b))
    if a < b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())

    parent = [0] * (n + 1)

    for i in range(1, n+1):
        connect = [0] + list(map(int, input().strip().split()))
        for j in range(1, n+1):
            if connect[j]:
                print("union %d %d" % (i, j))
                union(i, j)
                print(parent)

    print(parent)

    travel = list(map(int, input().strip().split()))

    root = find(travel[0])
    flag = True
    for i in range(1, m):
        if find(travel[i]) != root:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
