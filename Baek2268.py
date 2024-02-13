import sys
input = sys.stdin.readline


def merge(left, right):
    return left + right


def modify(left, right, node, idx, value):
    if idx < left or idx > right:
        return segTree[node]
    if left >= right:
        segTree[node] = value
        return segTree[node]

    mid = left + (right - left) // 2
    left_val = modify(left, mid, node * 2, idx, value)
    right_val = modify(mid + 1, right, (node * 2) + 1, idx, value)

    segTree[node] = merge(left_val, right_val)

    return segTree[node]


def query(left, right, node, query_left, query_right):
    if left > query_right or right < query_left:
        return 0
    if query_left <= left and right <= query_right:
        return segTree[node]

    mid = left + (right - left) // 2
    left_val = query(left, mid, node * 2, query_left, query_right)
    right_val = query(mid + 1, right, (node * 2) + 1, query_left, query_right)

    return merge(left_val, right_val)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    segTree = [0 for _ in range(4 * N)]

    for _ in range(M):
        token, a, b = map(int, input().strip().split())
        # Sum
        if token == 0:
            if a < b:
                print(query(1, N, 1, a, b))
            else:
                print(query(1, N, 1, b, a))
        # Modify
        elif token == 1:
            modify(1, N, 1, a, b)
