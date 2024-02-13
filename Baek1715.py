import sys, heapq
input = sys.stdin.readline

card = []
n = int(input().strip())

for _ in range(n):
    heapq.heappush(card, int(input().strip()))

res = 0
while card:
    if len(card) <= 1:
        break
    new_set = heapq.heappop(card) + heapq.heappop(card)
    res += new_set
    heapq.heappush(card, new_set)

print(res)
