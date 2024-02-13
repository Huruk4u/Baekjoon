import sys, heapq

input = sys.stdin.readline

heap = []
n = int(input().strip())

for _ in range(n):
    x = int(input().strip())
    if not x:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
