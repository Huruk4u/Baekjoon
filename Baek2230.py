import sys
input = sys.stdin.readline


def two_pointer(s, e, rtn):
    while s <= e < N:
        if A[e] - A[s] >= M:
            rtn = min(rtn, A[e] - A[s])
            s += 1
        else:
            if e == N-1:
                return rtn
            e += 1

    return rtn


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = [int(input().strip()) for _ in range(N)]
    A.sort()

    print(two_pointer(0, 1, A[N-1] - A[0]))
