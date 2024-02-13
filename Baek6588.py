import sys
input = sys.stdin.readline


def sieve():
    for i in range(2, N+1):
        if not odd_prime[i]:
            continue
        for j in range(i*2, N+1, i):
            if not odd_prime[j]:
                continue
            odd_prime[j] = False


if __name__ == '__main__':
    # N은 최대 1000000
    N = 1000000

    odd_prime = [False, False] + [True] * (N-1)
    sieve()

    # solve
    while True:
        ipt = int(input().strip())
        if not ipt:
            break
        flag = False
        for k in range(3, (ipt // 2) + 1, 2):
            if not odd_prime[k]:
                continue
            if odd_prime[ipt - k]:
                print("%d = %d + %d" % (ipt, k, ipt-k))
                flag = True
                break

        if not flag:
            print("Goldbach's conjecture is wrong.")
