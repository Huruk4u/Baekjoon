import sys

input = sys.stdin.readline


def preorder(curr):
    print(chr(curr + 65), end="")
    for child in tree[curr]:
        if child == '.':
            continue
        preorder(ord(child) - 65)


def inorder(curr):
    left, right = tree[curr]

    if left == right == '.':
        print(chr(curr+65), end="")
        return
    if left != '.':
        inorder(ord(left)-65)
    print(chr(curr+65), end="")
    if right != '.':
        inorder(ord(right)-65)


def postorder(curr):
    left, right = tree[curr]

    if left == right == '.':
        print(chr(curr + 65), end="")
        return

    for child in tree[curr]:
        if child == '.':
            continue
        postorder(ord(child) - 65)
    print(chr(curr+65), end="")


if __name__ == '__main__':
    # input
    n = int(input().strip())
    # tree
    tree = [[] for _ in range(n)]
    for _ in range(n):
        p, lc, rc = map(str, input().strip().split())
        tree[ord(p) - 65].append(lc)
        tree[ord(p) - 65].append(rc)

    preorder(0)
    print()
    inorder(0)
    print()
    postorder(0)

