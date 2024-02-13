import sys

input = sys.stdin.readline

# input
n, m = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# prefix_sum
prefix_sum = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]

"""
# test
print("")
for _ in range(n+1):
    print(prefix_sum[_])
"""
# solve
for _ in range(m):
    y1, x1, y2, x2 = map(int, input().strip().split())
    print(prefix_sum[y2][x2] - prefix_sum[y2][x1-1] - prefix_sum[y1-1][x2] + prefix_sum[y1-1][x1-1])