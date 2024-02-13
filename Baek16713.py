import sys

input = sys.stdin.readline

# input
n, q = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# prefix_xor
prefix_xor = [0] * (n+1)
for i in range(1, n+1):
    prefix_xor[i] = prefix_xor[i-1] ^ arr[i-1]

ans = 0
for _ in range(q):
    s, e = map(int, input().strip().split())
    ans ^= prefix_xor[e] ^ prefix_xor[s-1]

print(ans)
