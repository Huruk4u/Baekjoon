import sys

input = sys.stdin.readline

if __name__ == '__main__':
    is_prime = [True] * ((10 ** 6) + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, len(is_prime)):
        if not is_prime[i]: continue
        for j in range(i * 2, len(is_prime), i):
            is_prime[j] = False

    prime = []
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            prime.append(i)

    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        cnt = 0
        for i in prime:
            if i > (N // 2):
                break
            if is_prime[N - i]:
                cnt += 1

        print(cnt)

