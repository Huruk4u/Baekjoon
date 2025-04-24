import sys
input = sys.stdin.readline


def find(node):
    if parent[node] == node: return node
    parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    if root_x < root_y: parent[root_y] = root_x
    else: parent[root_x] = root_y


if __name__ == '__main__':
    N = int(input().strip())
    parent = [i for i in range(N+1)]

    for _ in range(N-2):
        u, v = map(int, input().strip().split())
        union(u, v)

    root_1 = find(1)
    root_target = 0
    for i in range(2, N+1):
        if find(i) != root_1:
            root_target = find(i)
            break

    print(root_1, root_target)
