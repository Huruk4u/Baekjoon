import sys
input = sys.stdin.readline


def find(node):
    if parent[node][0] == node:
        return parent[node]
    curr_root, dist_root = find(parent[node][0])
    parent[node] = [curr_root, parent[node][1] + dist_root]
    return parent[node]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return
    parent[root_x[0]] = [root_y[0], root_y[1] + abs(y - x) % 1000]


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        parent = [[i, 0] for i in range(N+1)]
        while True:
            ipt = list(input().strip().split())
            if ipt[0] == 'O': break
            if ipt[0] == 'I':
                u, v = int(ipt[1]), int(ipt[2])
                union(u, v)
            else:
                print(find(int(ipt[1]))[1])

