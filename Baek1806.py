import sys
input = sys.stdin.readline


def two_pointer(s, e, rtn):
    total = A[0]
    while s <= e < N+1:
        # print("-----------------------")
        # print("[%d : %d] total = %d" % (s, e, total))
        if total < S:
            if e == N:  # 더 탐색할 필요 없으면 return
                return rtn
            e += 1
            total += A[e-1]
        else:   # total >= S
            rtn = min(rtn, e-s)
            total -= A[s]
            s += 1

    return rtn


if __name__ == '__main__':
    N, S = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    ans = two_pointer(0, 1, N+1)

    if ans == N+1:
        print(0)
    else:
        print(ans)
