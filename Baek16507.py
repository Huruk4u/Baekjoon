import sys

input = sys.stdin.readline

# input
r, c, q = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(r)]

# prefix_sum, 1,000,000
prefix_sum = [[0] * (c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1, c+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]

# 10,000
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().strip().split())

    div_n = (r2-r1+1) * (c2-c1+1)
    part_sum = prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]

    print(part_sum // div_n)
