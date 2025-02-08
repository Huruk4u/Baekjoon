import sys
from itertools import combinations
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    S = [list(map(int, input().strip().split())) for _ in range(N)]

    start_team = list(combinations([i for i in range(N)], N//2))
    rtn = sys.maxsize

    sum_stat = [0 for i in range(N)]
    for i in range(N):
        for j in range(N):
            sum_stat[i] += S[i][j]
            sum_stat[j] += S[i][j]

    total_stat = sum(sum_stat) // 2
    for start in combinations(sum_stat, N//2):
        rtn = min(rtn, abs(total_stat - sum(start)))

    print(rtn)
