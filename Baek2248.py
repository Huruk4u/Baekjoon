import sys
input = sys.stdin.readline


def count(n, m):
    # memoization
    if cnt[n][m]:
        return cnt[n][m]
    # 채워야 할 비트 수가 끝자리에 도달하거나, 모든 1을 사용한 경우
    if n == 0 or m == 0:
        return 1

    cnt[n][m] = count(n-1, m) + count(n-1, m-1)
    return cnt[n][m]


def binary(n, m, pivot):
    print("===========================")
    print("%d %d %d" % (n, m, pivot))
    if n == 0:
        return ''
    if m >= 1:
        i = count(n-1, m)
        print("i = %d" % i)
        if pivot <= i:
            print("%d번째 자리엔 0채움" % (N-n))
            return '0' + binary(n-1, m, pivot)
        else:
            print("%d번째 자리엔 1채움" % (N-n))
            return '1' + binary(n-1, m-1, pivot-i)
    else:
        print("모든 m을 채웠으니 0채움")
        return '0' + binary(n-1, m, pivot)


if __name__ == '__main__':
    N, L, I = map(int, input().strip().split())
    cnt = [[0] * (L+1) for _ in range(N+1)]

    print(binary(N, L, I))
