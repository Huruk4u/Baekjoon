import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(x, y):
    if (0 <= x < N) and (0 <= y < M):
        return True
    else:
        return False


def dijkstra():
    heap = [[dist[0][0], 0, 0]]
    while heap:
        dist_curr, cx, cy = heapq.heappop(heap)
        if cx == N-1 and cy == M-1:
            return dist[M-1][N-1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not in_range(nx, ny):
                continue
            if dist_curr + matrix[ny][nx] < dist[ny][nx]:
                dist[ny][nx] = dist_curr + matrix[ny][nx]
                heapq.heappush(heap, [dist[ny][nx], nx, ny])
    return dist[M-1][N-1]


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(map(int, input().strip())) for _ in range(M)]

    dist = [[INF] * N for _ in range(M)]
    dist[0][0] = 0

    print(dijkstra())
