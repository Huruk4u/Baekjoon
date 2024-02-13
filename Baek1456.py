import sys
input = sys.stdin.readline


def sieve(N):
    for i in range(N+1):
        if not is_prime[i]:
            continue
        prime.append(i)

        for j in range(i*2, N+1, i):
            if not is_prime[j]:
                continue
            is_prime[j] = False


if __name__ == '__main__':
    A, B = map(int, input().strip().split())

    N = int(B**(1/2)) + 1
    is_prime = [False, False] + [True] * (N-1)
    prime = []

    sieve(N)

    cnt = 0
    # solve
    for k in prime:
        k_square = k * k
        while True:
            if k_square > B:
                break
            elif A <= k_square <= B:
                cnt += 1
            k_square *= k

    print(cnt)
