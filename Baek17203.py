import sys

input = sys.stdin.readline

# input
n, q = map(int, input().strip().split())
melody = list(map(int, input().strip().split()))

# delta
delta = []
for idx in range(1, n):
    delta.append(abs(melody[idx] - melody[idx-1]))

# prefix_sum
prefix_sum = [0] * n
for idx in range(1, n):
    prefix_sum[idx] = prefix_sum[idx-1] + delta[idx-1]

for _ in range(q):
    i, j = map(int, input().strip().split())

    print(prefix_sum[j-1] - prefix_sum[i-1])
