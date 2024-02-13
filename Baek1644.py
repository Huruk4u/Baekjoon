import sys
input = sys.stdin.readline


def sieve():
    for i in range(2, N+1):
        if not is_prime[i]:
            continue
        prime.append(i)
        for j in range(i*2, N+1, i):
            if not is_prime[j]:
                continue
            is_prime[j] = False


def two_pointer(s, e, total):
    cnt = 0
    while s <= e:
        if total == N:
            cnt += 1
            total -= prime[s]
            s += 1
        elif total > N:
            total -= prime[s]
            s += 1
        else:
            if e == len(prime):
                return cnt
            else:
                e += 1
                total += prime[e - 1]

    return cnt


if __name__ == '__main__':
    N = int(input().strip())

    # sieve
    is_prime = [False, False] + [True] * (N-1)
    prime = []
    sieve()

    # two pointer
    print(two_pointer(0, 0, 0))
