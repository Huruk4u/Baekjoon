import sys
input = sys.stdin.readline


def sieve(N):
    for i in range(2, N+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, N+1, i):
            if not is_prime[j]:
                continue
            is_prime[j] = False


def solve(K):
    left = 0
    left_idx = K - 1
    while left == 0:
        if is_prime[left_idx]:
            left = left_idx
        else:
            left_idx -= 1
    right = 0
    right_idx = K + 1
    while right == 0:
        if is_prime[right_idx]:
            right = right_idx
        else:
            right_idx += 1

    return right - left


if __name__ == '__main__':
    T = int(input().strip())

    N = 1299709
    is_prime = [False, False] + [True] * (N-1)
    sieve(N)

    # solve
    for _ in range(T):
        K = int(input().strip())
        if is_prime[K]:
            print(0)
        else:
            print(solve(K))
