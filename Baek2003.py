import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))

    s = e = 0
    cnt = 0
    total = 0
    while True:
        if s == N:
            break
        if total == M:
            cnt += 1
            total -= A[s]
            s += 1
            continue
        if e == N or total > M:
            total -= A[s]
            s += 1
            continue
        if s == e or total < M:
            e += 1
            total += A[e-1]
            continue

    print(cnt)
