import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    S = list(map(int, input().strip().split()))

    left, right = [1] * N, [1] * N
    # left
    for k in range(N):
        max_length = 0
        # S[0] ~ S[k-1]
        for i in range(k):
            if S[i] < S[k]:
                max_length = max(max_length, left[i])
        left[k] += max_length
    # right
    for k in range(N-1, -1, -1):
        max_length = 0
        # S[k+1] ~ S[N-1]
        for i in range(N-1, k, -1):
            if S[i] < S[k]:
                max_length = max(max_length, right[i])
        right[k] += max_length

    # 최대 길이 출력
    result = 0
    for k in range(N):
        result = max(result, left[k] + right[k] - 1)

    print(result)