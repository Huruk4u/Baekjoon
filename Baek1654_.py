import sys
input = sys.stdin.readline


def bs(low, high):
    mid = (high + low) // 2
    if low > high:
        return mid
    # print("%d == %d == %d" % (low, mid, high))
    rtn = 0
    for l in lan:
        rtn += l // mid

    if rtn >= N:
        return bs(mid+1, high)
    else:
        return bs(low, mid-1)


if __name__ == '__main__':
    K, N = map(int, input().strip().split())
    lan = [int(input().strip()) for _ in range(K)]

    print(bs(1, max(lan)))
