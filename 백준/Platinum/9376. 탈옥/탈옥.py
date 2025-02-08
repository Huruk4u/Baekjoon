import sys, heapq
from pprint import pprint

input = sys.stdin.readline
INF = sys.maxsize

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    if (0 <= y < H+2) and (0 <= x < W+2):
        return True
    else:
        return False


def dijkstra(heap):
    cost = [[INF] * (W+2) for _ in range(H+2)]
    cost[heap[0][1]][heap[0][2]] = 0
    # print(heap)
    while heap:
        curr_cost, cy, cx = heapq.heappop(heap)
        if cost[cy][cx] < curr_cost:
            continue
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not in_range(ny, nx): continue
            if matrix[ny][nx] == '*':
                continue
            elif matrix[ny][nx] in ('.', '$'):
                if cost[ny][nx] > cost[cy][cx]:
                    cost[ny][nx] = cost[cy][cx]
                    heapq.heappush(heap, (cost[ny][nx], ny, nx))
            elif matrix[ny][nx] == '#':
                if cost[ny][nx] > cost[cy][cx] + 1:
                    cost[ny][nx] = cost[cy][cx] + 1
                    heapq.heappush(heap, (cost[ny][nx], ny, nx))
    return cost


def masking(cost):
    for y in range(H+2):
        for x in range(W+2):
            if cost[y][x] == INF:
                cost[y][x] = 'X'
            else:
                cost[y][x] = str(cost[y][x])
    return cost


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        # user input 처리 및 초기 설정
        H, W = map(int, input().strip().split())
        ipt_matrix = [list(input().strip()) for _ in range(H)]

        matrix = [['.' for _ in range(W+2)] for _ in range(H+2)]
        starting_point = [(0, 0)]
        for y in range(H):
            for x in range(W):
                matrix[y+1][x+1] = ipt_matrix[y][x]
                if matrix[y+1][x+1] == '$':
                    starting_point.append((y+1, x+1))

        # print(starting_point)
        cost_1 = dijkstra([(0, starting_point[0][0], starting_point[0][1])])
        cost_2 = dijkstra([(0, starting_point[1][0], starting_point[1][1])])
        cost_3 = dijkstra([(0, starting_point[2][0], starting_point[2][1])])
        # pprint(masking(cost_1))
        # pprint(masking(cost_2))
        # pprint(masking(cost_3))
        answer = INF
        for y in range(1, H+1):
            for x in range(1, W+1):
                if matrix[y][x] == '*':
                    continue
                # total_cost = 외부에서 내부로 접근 + 죄수1의 경로 + 죄수2의 경로
                total_cost = cost_1[y][x] + cost_2[y][x] + cost_3[y][x]
                # 문에 해당하면 2번은 더 땄을거니까-2
                if matrix[y][x] == '#':
                    total_cost -= 2
                answer = min(answer, total_cost)

        print(answer)
