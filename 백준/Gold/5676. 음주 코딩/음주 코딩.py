import sys
input = sys.stdin.readline


def merge(left, right):
    return left * right


def define(node_number, left, right):
    if left == right:
        if A[left-1] > 0:
            tree[node_number] = 1
        elif A[left-1] < 0:
            tree[node_number] = -1
        else:
            tree[node_number] = 0
        return tree[node_number]

    mid = left + (right - left) // 2
    left_val = define(node_number * 2, left, mid)
    right_val = define(node_number * 2 + 1, mid + 1, right)

    tree[node_number] = merge(left_val, right_val)
    return tree[node_number]


def query(node_number, left, right, query_left, query_right):
    if query_right < left or right < query_left:
        return 1
    if query_left <= left and right <= query_right:
        return tree[node_number]

    mid = left + (right - left) // 2
    left_val = query(node_number * 2, left, mid, query_left, query_right)
    right_val = query(node_number * 2 + 1, mid + 1, right, query_left, query_right)

    return merge(left_val, right_val)


def update(node_number, left, right, idx, value):
    if idx < left or idx > right:
        return tree[node_number]
    if left == right:
        tree[node_number] = value
        return tree[node_number]

    mid = left + (right - left) // 2
    left_val = update(node_number * 2, left, mid, idx, value)
    right_val = update(node_number * 2 + 1, mid+1, right, idx, value)

    tree[node_number] = merge(left_val, right_val)
    return tree[node_number]


if __name__ == '__main__':
    while True:
        try:
            N, K = map(int, input().strip().split())
        except Exception:
            break

        A = list(map(int, input().strip().split()))

        tree = [0] * ((4 * N) + 1)
        define(1, 1, N)
        result = []
        for i in range(K):
            token, I, V = map(str, input().strip().split())
            I, V = int(I), int(V)
            if token == 'C':
                if V > 0:
                    V = 1
                elif V < 0:
                    V = -1
                update(1, 1, N, I, V)
            else:
                rtn = query(1, 1, N, I, V)
                if rtn > 0:
                    result.append('+')
                elif rtn < 0:
                    result.append('-')
                else:
                    result.append('0')

        print("".join(result))
