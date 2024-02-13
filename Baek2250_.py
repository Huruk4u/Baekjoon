import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000001)


def inorder(curr, level):
    global col
    left, right = tree[curr]
    if left:
        inorder(left, level+1)
    if not width[level][0]:  # if left x not updated
        width[level][0] = col
    width[level][1] = col
    col += 1
    if right:
        inorder(right, level+1)


def get_tree(n):
    for _ in range(n):
        num, l, r = map(int, input().strip().split())
        if l != -1:
            if is_root[l]:
                is_root[l] = False
            tree[num][0] = l
        if r != -1:
            if is_root[r]:
                is_root[r] = False
            tree[num][1] = r


if __name__ == '__main__':
    n = int(input().strip())
    is_root = [True] * (n+1)

    # tree
    tree = [[0, 0] for _ in range(n + 1)]
    get_tree(n)

    # find root
    root = 0
    for i in range(1, n+1):
        if is_root[i]:
            root = i

    col = 1
    width = [[0, 0] for _ in range(n + 1)]

    inorder(root, 1)

    ans = width[1][1] - width[1][0] + 1
    ans_lev = 1
    for lev in range(2, n + 1):
        if width[lev]:
            w = width[lev][1] - width[lev][0] + 1
            if ans < w:
                ans = w
                ans_lev = lev

    print(ans_lev, ans)
