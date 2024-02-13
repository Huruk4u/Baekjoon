import sys, heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    x = int(input().strip())
    if not x:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
