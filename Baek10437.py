import sys, heapq
input = sys.stdin.readline
INF = float(sys.maxsize)


# 거리 계산 함수
def distance_calculator(x1, y1, x2, y2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2

    return (x+y) ** 0.5


def dijkstra():
    global weight
    heap = [(weight[0], 0)]
    while heap:
        weight_curr, curr_locate = heapq.heappop(heap)
        cx, cy = locate[curr_locate]
        print("---------------------------------------")
        print("현재 위치 (%f, %f)" % (cx, cy))
        if cx == dst_x and cy == dst_y:
            return weight[N+1]

        for next in range(1, N+2):
            nx, ny = locate[next]
            # 현재 위치가 대포라면
            if 1 <= curr_locate <= N:
                new_dist_next = distance_calculator(cx, cy, nx, ny)
                new_dist_next = min(new_dist_next, abs(new_dist_next - 50))

                weight_new = (new_dist_next / velocity) + 2

                if weight_curr + weight_new < weight[next]:
                    print("(%f, %f) -------- %f --------> (%f, %f)" % (cx, cy, weight_curr + weight_new, nx, ny))
                    weight[next] = weight_curr + weight_new
                    heapq.heappush(heap, (weight[next], next))
            else:
                new_dist_next = distance_calculator(cx, cy, nx, ny)
                weight_new = new_dist_next / velocity

                if weight_curr + weight_new < weight[next]:
                    print("(%f, %f) -------- %f --------> (%f, %f)" % (cx, cy, weight_curr + weight_new, nx, ny))
                    weight[next] = weight_curr + weight_new
                    heapq.heappush(heap, (weight[next], next))
        print(weight)
    return weight[N+1]


if __name__ == '__main__':
    start_x, start_y = map(float, input().strip().split())
    dst_x, dst_y = map(float, input().strip().split())
    N = int(input().strip())

    velocity = 5

    # 노드 위치 정보
    locate = [[0, 0] for _ in range(N+2)]
    locate[0] = [start_x, start_y]
    locate[N+1] = [dst_x, dst_y]

    for i in range(1, N+1):
        x, y = map(float, input().strip().split())
        locate[i] = [x, y]

    # 노드 별 거리 정보
    weight = [INF] * (N + 2)
    weight[0] = 0

    print(locate)
    print(dijkstra())
