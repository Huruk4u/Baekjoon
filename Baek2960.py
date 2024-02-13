import sys
input = sys.stdin.readline


def solve(N, K):
    cnt = 1

    for i in range(2, N+1):
        if is_prime[i]:
            if cnt == K:
                return i
            cnt += 1
            for j in range(i*2, N+1, i):
                if is_prime[j]:
                    is_prime[j] = False
                    if cnt == K:
                        return j
                    cnt += 1


if __name__ == '__main__':
    N, K = map(int, input().strip().split())

    is_prime = [False, False] + ([True] * (N-1))

    print(solve(N, K))
