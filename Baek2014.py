import sys, heapq

input = sys.stdin.readline
sys.setrecursionlimit(10000001)


def solve(prev, x):
    global cnt
    if cnt == n:
        print(x)
        return
    if x == prev:
        solve(x, heapq.heappop(heap))
        return

    for i in range(k):
        heapq.heappush(heap, x * prime[i])
        if x % prime[i] == 0:
            break

    cnt += 1
    print(cnt, heap)
    solve(x, heapq.heappop(heap))


if __name__ == '__main__':
    # input
    k, n = map(int, input().strip().split())
    prime = list(map(int, input().strip().split()))
    prime.sort()

    # heap
    heap = prime[:]
    cnt = 1

    solve(0, heapq.heappop(heap))
