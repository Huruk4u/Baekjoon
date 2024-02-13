import sys

input = sys.stdin.readline


def preorder(curr):
    global leaf

    if not tree[curr]:
        leaf += 1
        return

    for child in tree[curr]:
        preorder(child)

    return


if __name__ == '__main__':
    n = int(input().strip())
    # root, tree, n of leaf
    no_root = False
    root = int
    leaf = 0
    tree = [[] for _ in range(n)]
    # input
    parent = list(map(int, input().strip().split()))
    x = int(input().strip())

    for i in range(n):
        if i == x:
            if parent[i] == -1:
                no_root = True
            continue
        if parent[i] == -1:
            root = i
            continue
        tree[parent[i]].append(i)

    if no_root:
        print(0)
    else:
        preorder(root)
        print(leaf)
