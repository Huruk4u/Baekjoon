import sys, heapq

input = sys.stdin.readline

INF = sys.maxsize
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    if (0 <= x < N) and (0 <= y < N):
        return True
    else:
        return False


def dijkstra():
    while heap:
        dist_curr, cx, cy = heapq.heappop(heap)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not in_range(nx, ny):
                continue
            if dist_curr + matrix[ny][nx] < dist[ny][nx]:
                dist[ny][nx] = dist_curr + matrix[ny][nx]
                heapq.heappush(heap, [dist[ny][nx], nx, ny])
    return


if __name__ == '__main__':
    cnt = 1

    while True:
        N = int(input().strip())
        if not N:
            break

        matrix = [list(map(int, input().strip().split())) for _ in range(N)]
        dist = [[INF] * N for _ in range(N)]
        dist[0][0] = matrix[0][0]
        heap = [[dist[0][0], 0, 0]]

        dijkstra()
        print("Problem %d: %d" % (cnt, dist[N - 1][N - 1]))

        cnt += 1
