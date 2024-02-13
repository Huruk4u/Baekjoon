import sys
input = sys.stdin.readline


def exp_simulation(K):
    total = 0
    cnt = 1
    for i in range(N):
        # 예산이 지출보다 많은 경우
        if total + exp[i] > K:
            cnt += 1
            total = 0
        # 예산이 지출보다 적을 경우
        total += exp[i]

    return cnt


def bs(low, high):
    mid = (low + high) // 2
    if low >= high:
        return mid

    cnt = exp_simulation(mid)

    if cnt <= M:
        return bs(low, mid)
    else:
        return bs(mid+1, high)


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    exp = [int(input().strip()) for _ in range(N)]

    print(bs(max(exp), sum(exp) + 1))
