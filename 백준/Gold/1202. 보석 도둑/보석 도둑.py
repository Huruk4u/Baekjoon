import sys, heapq
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    gem = []  # gem heap
    for _ in range(N):
        weight, price = map(int, input().strip().split())
        heapq.heappush(gem, (weight, price))

    bags = sorted([int(input().strip()) for _ in range(K)])
    heap = []
    bag_idx, rtn = 0, []
    for bag in bags:
        # 가방의 용량이 보석의 무게보다 작아질 때까지, 모든 보석을 heap에 담는다.
        while gem and bag >= gem[0][0]:
            heapq.heappush(heap, -heapq.heappop(gem)[1])
        if heap:
            rtn.append(-heapq.heappop(heap))
        else:
            if not gem:
                break

    print(sum(rtn))
