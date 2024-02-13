import sys

input = sys.stdin.readline


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
    if x < y:
        parent[root_y] = root_x
        friends[root_x] += friends[root_y]
    else:
        parent[root_x] = root_y
        friends[root_y] += friends[root_x]


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())

        parent = dict()
        friends = dict()

        for _ in range(n):
            a, b = map(str, input().strip().split())

            if a not in parent:
                parent[a] = a
                friends[a] = 1
            if b not in parent:
                parent[b] = b
                friends[b] = 1

            union(a, b)
            print(friends[find(a)])
