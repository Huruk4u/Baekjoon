import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    dolsang = list(map(int, input().strip().split()))

    prefix_left = [0] * N
    prefix_right = [0] * N
    if dolsang[0] == 1:
        prefix_left[0] = 1
    else:
        prefix_right[0] = 1

    # prefix_left
    for i in range(1, N):
        if dolsang[i] == 1:
            prefix_left[i] = prefix_left[i-1] + 1
        else:
            prefix_left[i] = prefix_left[i-1] - 1 if prefix_left[i-1] > 0 else 0

    # prefix_right
    for i in range(1, N):
        if dolsang[i] == 2:
            prefix_right[i] = prefix_right[i-1] + 1
        else:
            prefix_right[i] = prefix_right[i-1] - 1 if prefix_right[i-1] > 0 else 0

    print(max(max(prefix_left), max(prefix_right)))
