import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)


def postorder(curr):
    global res

    left, right = tree[curr]
    if left:
        postorder(tree[curr][0])
    if right:
        postorder(tree[curr][1])

    res.append(curr)
    return


def to_tree(curr, preord, inord):
    if not inord or not preord:
        return
    curr_idx = inord.index(curr)

    left_child = inord[:curr_idx]
    right_child = inord[curr_idx+1:]
    left_preord = preord[1:len(left_child)+1]
    right_preord = preord[len(left_child)+1:]

    if left_child:
        tree[curr][0] = left_preord[0]
        to_tree(left_preord[0], left_preord, left_child)
    if right_child:
        tree[curr][1] = right_preord[0]
        to_tree(right_preord[0], right_preord, right_child)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        # input
        n = int(input().strip())
        preorder = list(map(int, input().strip().split()))
        inorder = list(map(int, input().strip().split()))
        root = preorder[0]
        # tree
        tree = [[0, 0] for _ in range(n+1)]
        to_tree(root, preorder, inorder)

        res = []

        postorder(root)
        print(*res)
