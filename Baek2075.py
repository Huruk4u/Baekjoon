import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    ipt = list(map(int, input().strip().split()))
    if not heap:
        for i in range(n):
            heapq.heappush(heap, ipt[i])
    else:
        for i in range(n):
            if heap[0] < ipt[i]:
                heapq.heappush(heap, ipt[i])
                heapq.heappop(heap)

print(heapq.heappop(heap))
