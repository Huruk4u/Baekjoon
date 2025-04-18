import sys, heapq
from pprint import pprint
input = sys.stdin.readline
INF = sys.maxsize

# 상, 좌, 하, 우순 델타
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def in_range(y, x):
    return (0 <= y < N) and (0 <= x < N)


def dijkstra(heap):
    while heap:
        dist_curr, cy, cx, delta = heapq.heappop(heap)
        if cy == ty and cx == tx:
            return dist_curr

        if dist[cy][cx][delta] < dist_curr:
            continue

        # print("%d %d %d visited" % (cy, cx, delta))

        ny, nx = cy + dy[delta], cx + dx[delta]
        if not in_range(ny, nx) or matrix[ny][nx] == '*': continue
        if dist[ny][nx][delta] <= dist[cy][cx][delta]: continue

        # 직진 : 현재 델타를 그대로 유지한 채로 진행함. 가중치 + 1 없음
        dist[ny][nx][delta] = dist[cy][cx][delta]
        heapq.heappush(heap, (dist[ny][nx][delta], ny, nx, delta))

        # 다음 진행방향이 거울이면, 델타에 변화를 준 채로 가중치 + 1
        if matrix[ny][nx] == '!':
            dist[ny][nx][(delta+1) % 4] = dist[cy][cx][delta] + 1
            heapq.heappush(heap, (dist[ny][nx][(delta+1) % 4], ny, nx, (delta+1) % 4))

            dist[ny][nx][(delta-1) % 4] = dist[cy][cx][delta] + 1
            heapq.heappush(heap, (dist[ny][nx][(delta-1) % 4], ny, nx, (delta-1) % 4))
    return -1


if __name__ == '__main__':
    N = int(input().strip())
    matrix = [list(input().strip()) for _ in range(N)]

    sy, sx = 0, 0
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == '#':
                sy, sx = y, x

    ty, tx = 0, 0
    for y in range(N):
        for x in range(N):
            if y == sy and x == sx: continue
            if matrix[y][x] == '#':
                ty, tx = y, x

    # heap[0] : y, x, d에 도달하기 위해 설치하는 최소 거울 갯수, y좌표, x좌표, y, x에 도달하기 위한 delta
    heap = [(0, sy, sx, 0), (0, sy, sx, 1), (0, sy, sx, 2), (0, sy, sx, 3)]

    dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    dist[sy][sx][0] = 0
    dist[sy][sx][1] = 0
    dist[sy][sx][2] = 0
    dist[sy][sx][3] = 0

    print(dijkstra(heap))
