import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def postorder(curr, level):
    left, right = tree[curr]
    if not left and not right:
        # print("visited %d" % curr)
        # print("weight = %d" % 1)
        return 1
    elif not right:
        left_weight = postorder(left, level+1)
        # print("visited %d" % curr)
        # print("weight = %d" % (left_weight + 1))
        weight[curr] = [left_weight, 0]
        return left_weight + 1
    elif not left:
        right_weight = postorder(right, level+1)
        # print("visited %d" % curr)
        # print("weight = %d" % (right_weight + 1))
        weight[curr] = [0, right_weight]
        return right_weight + 1
    else:
        left_weight = postorder(left, level+1)
        right_weight = postorder(right, level+1)
        weight[curr] = [left_weight, right_weight]
        # print("visited %d" % curr)
        # print("weight = %d" % (left_weight + right_weight + 1))
        return left_weight + right_weight + 1


def inorder(curr, level):
    global col
    left, right = tree[curr]
    if not left and not right:
        print("visited %d" % curr)
        if not x[level][0]:     # if left x not updated
            x[level][0] = col
        x[level][1] = col
        col += 1
        return
    elif not right:
        inorder(left, level+1)
        print("visited %d" % curr)
        if not x[level][0]:
            x[level][0] = col
        x[level][1] = col
        col += 1
        return
    elif not left:
        inorder(right, level+1)
        print("visited %d" % curr)
        if not x[level][0]:
            x[level][0] = col
        x[level][1] = col
        col += 1
        return
    else:
        inorder(left, level+1)
        print("visited %d" % curr)
        if not x[level][0]:
            x[level][0] = col
        x[level][1] = col
        col += 1
        inorder(right, level+1)
        return


if __name__ == '__main__':
    n = int(input().strip())
    tree = [[] for _ in range(n+1)]
    for _ in range(n):
        n, l, r = map(int, input().strip().split())
        if l == -1 and r == -1:
            tree[n] = [0, 0]
        elif l == -1:
            tree[n] = [0, r]
        elif r == -1:
            tree[n] = [l, 0]
        else:
            tree[n] = [l, r]

    col = 1
    weight = [[0, 0] for _ in range(n+1)]
    x = [[0, 0] for _ in range(n+1)]
    # node number, current level
    # postorder(1, 1)
    inorder(1, 1)

    print(weight)

    print(x)