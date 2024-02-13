import sys
input = sys.stdin.readline


def to_value(list_k):
    rtn = 0
    list_k = map(int, list_k)
    for n in list_k:
        rtn += n*n
    return rtn


def sieve(N):
    for i in range(2, N+1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, N + 1, i):
            if not is_prime[j]:
                continue
            is_prime[j] = False


if __name__ == '__main__':
    N = int(input().strip())
    is_prime = [False, False] + [True] * (N-1)
    sieve(N)

    # 1부터 N까지의 loop
    for k in range(1, N+1):
        # k가 소수가 아니라면 pass
        if not is_prime[k]:
            continue

        # 상근수 전개하면서 나온 숫자 집합
        value_set = set()
        value = k
        while True:
            value = to_value(list(str(value)))
            if value == 1:
                print(k)
                break
            if value in value_set:
                break
            value_set.add(value)
