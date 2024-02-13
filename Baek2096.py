import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())

    # 이전 row의 최대 값
    dp_max = [0, 0, 0]
    dp_min = [0, 0, 0]
    for _ in range(N):
        A = list(map(int, input().strip().split()))
        max_0 = max(dp_max[0], dp_max[1]) + A[0]
        max_1 = max(dp_max[0], dp_max[1], dp_max[2]) + A[1]
        max_2 = max(dp_max[1], dp_max[2]) + A[2]

        dp_max[0] = max_0
        dp_max[1] = max_1
        dp_max[2] = max_2

        min_0 = min(dp_min[0], dp_min[1]) + A[0]
        min_1 = min(dp_min[0], dp_min[1], dp_min[2]) + A[1]
        min_2 = min(dp_min[1], dp_min[2]) + A[2]

        dp_min[0] = min_0
        dp_min[1] = min_1
        dp_min[2] = min_2

    print(max(dp_max), min(dp_min))
