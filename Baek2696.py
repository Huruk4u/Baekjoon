import sys, heapq

input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        # input
        n = int(input().strip())
        arr = []
        if (n % 10) == 0:
            for _ in range(n//10):
                arr += list(map(int, input().strip().split()))
        else:
            for _ in range((n // 10) + 1):
                arr += list(map(int, input().strip().split()))

        # left = max heap, right = min heap
        mid, left, right = arr[0], [], []
        ans = [mid]

        # solve
        for i in range(1, n):
            if arr[i] < mid:
                heapq.heappush(left, -arr[i])
            else:
                heapq.heappush(right, arr[i])

            # even
            if i % 2 == 1:
                if len(left) > len(right):
                    heapq.heappush(right, mid)
                else:
                    heapq.heappush(left, -mid)
            # odd
            else:
                if len(left) > len(right):
                    mid = -heapq.heappop(left)
                else:
                    mid = heapq.heappop(right)
                ans.append(mid)

        # print
        print(len(ans))
        for i in range(len(ans)):
            if (i + 1) != 1 and (i + 1) % 10 == 1:
                print()
            print(ans[i], end=' ')
        print()
