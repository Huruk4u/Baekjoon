import sys
input = sys.stdin.readline


def count(n, m):
    if cnt[n][m]:
        return cnt[n][m]
    if n == 0 or m == 0:
        return 1

    cnt[n][m] = count(n-1, m) + count(n-1, m-1)
    return cnt[n][m]


def binary(n, m, pivot):
    if n == 0:
        return ''
    if m >= 1:
        i = count(n-1, m)
        if pivot <= i:
            return '0' + binary(n-1, m, pivot)
        else:
            return '1' + binary(n-1, m-1, pivot-i)
    else:
        return '0' + binary(n-1, m, pivot)


if __name__ == '__main__':
    N, L, I = map(int, input().strip().split())
    cnt = [[0] * (L+1) for _ in range(N+1)]

    print(binary(N, L, I))
