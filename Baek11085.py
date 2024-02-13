import sys
input = sys.stdin.readline


def is_capital(root):
    if root == baek or root == cube:
        return True
    else:
        return False


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    global flag
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    if is_capital(root_a) and is_capital(root_b):
        flag = True
        parent[root_b] = root_a
    elif is_capital(root_a):
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


if __name__ == '__main__':
    # input
    node, n = map(int, input().strip().split())
    baek, cube = map(int, input().strip().split())
    edge = [list(map(int, input().strip().split())) for _ in range(n)]

    edge = sorted(edge, key=lambda x: -x[2])
    parent = [i for i in range(node)]
    flag = False

    for a, b, weight in edge:
        union(a, b)
        if flag:
            print(weight)
            break
