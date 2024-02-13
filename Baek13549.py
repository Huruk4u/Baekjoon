import sys, heapq

input = sys.stdin.readline


def in_range(x):
    if 0 <= x <= 100000:
        return True
    else:
        return False


def bfs(heap):
    while heap:
        cnt, cx = heapq.heappop(heap)

        visited[cx] = True

        if cx == K:
            return cnt

        nx = [cx-1, cx+1, cx*2]
        for i in range(3):
            # 범위 안에 들지 않으면 고려 X
            if not in_range(nx[i]) or visited[nx[i]]:
                continue

            if i == 2:
                heapq.heappush(heap, (cnt, nx[i]))
            else:
                heapq.heappush(heap, (cnt + 1, nx[i]))

    return 0


if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    heap = [(0, N)]
    visited = [False] * 100001

    print(bfs(heap))
