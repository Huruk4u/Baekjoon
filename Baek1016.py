import sys
input = sys.stdin.readline


def sieve():
    cnt = 0
    for i in range(2, N+1):
        sqr_i = i * i
        for j in range((((A-1) // sqr_i) + 1) * sqr_i, B+1, sqr_i):
            # 이미 제곱 ㄴㄴ수로 판정이 된 경우
            if not square_ss[j - A]:
                continue
            square_ss[j - A] = False
            cnt += 1

    return cnt


if __name__ == '__main__':
    A, B = map(int, input().strip().split())
    N = int(B ** 0.5)

    # A부터 B 사이의 제곱 ㄴㄴ수
    square_ss = [True] * (B - A + 1)

    print((B - A + 1) - sieve())
