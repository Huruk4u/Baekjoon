import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    date = list(map(int, input().strip().split()))

    s = 1
    e = K
    # 초기 window_sum 설정
    ans = 0
    for i in range(K):
        ans += date[i]

    window_sum = ans
    while e < N:
        window_sum -= date[s-1]
        window_sum += date[e]

        ans = max(ans, window_sum)
        s += 1
        e += 1

    print(ans)
