import sys
input = sys.stdin.readline

mod = 1000000007


def merge(left, right):
    return (left * right) % mod


def define(left, right, node):
    # leaf_node 에 도달 시
    if left == right:
        segTree[node] = num[left-1]
        return segTree[node]

    # recursion part
    mid = left + (right - left) // 2
    left_val = define(left, mid, node * 2)
    right_val = define(mid+1, right, (node * 2) + 1)

    segTree[node] = merge(left_val, right_val)
    return segTree[node]


def update(left, right, node, idx, update_val):
    # idx가 범위에 들지 못하면 return
    if idx < left or idx > right:
        return segTree[node]
    # 목적지 도달
    if left == right:
        segTree[node] = update_val
        return segTree[node]

    # recursion part
    mid = left + (right - left) // 2
    left_val = update(left, mid, node * 2, idx, update_val)
    right_val = update(mid + 1, right, (node * 2) + 1, idx, update_val)

    segTree[node] = merge(left_val, right_val)
    return segTree[node]


def query(left, right, node, query_left, query_right):
    global ans
    print("--------------------------------")
    print("%d %d : %d %d" % (left, right, query_left, query_right))
    # 범위가 완전히 벗어나는 경우
    if query_left > right or query_right < left:
        print("no return")
        return 1
    # 범위가 완전히 포함되는 경우
    if query_left <= left and right <= query_right:
        print("return seg")
        return segTree[node]

    mid = left + (right - left) // 2
    left_val = query(left, mid, node * 2, query_left, query_right)
    right_val = query(mid + 1, right, (node * 2) + 1, query_left, query_right)

    print("value : %d %d" % (left_val, right_val))
    ans = merge(left_val, right_val)
    print("ans = %d" % ans)

    return ans


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())

    num = []
    for _ in range(N):
        num.append(int(input().strip()))

    # define segTree
    segTree = [0 for _ in range(4*N)]
    define(1, N, 1)
    print()
    print(segTree)
    for _ in range(M+K):
        a, b, c = map(int, input().strip().split())
        if a == 1:
            update(1, N, 1, b, c)
            print(segTree)
        elif a == 2:
            ans = 1
            print(query(1, N, 1, b, c))
