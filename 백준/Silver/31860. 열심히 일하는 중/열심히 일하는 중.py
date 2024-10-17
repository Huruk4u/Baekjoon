import sys, heapq
input = sys.stdin.readline


if __name__ == '__main__':
    N, M, K = map(int, input().strip().split())
    heap = []
    for _ in range(N):
        heapq.heappush(heap, -int(input().strip()))

    rtn = [0]
    while heap:
        task = -heapq.heappop(heap)
        rtn.append((rtn[-1]//2) + task)
        if task - M > K:
            heapq.heappush(heap, -(task - M))

    print(len(rtn) - 1)
    for i in range(1, len(rtn)):
        print(rtn[i])
