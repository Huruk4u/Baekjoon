import sys, heapq
from pprint import pprint
INF = sys.maxsize


def solution(board):
    
    def in_range(x, y):
        if (0 <= x < N) and (0 <= y < N):
            return True
        else:
            return False
        
    def dijkstra(heap):
        while heap:
            curr_cost, direction, cy, cx = heapq.heappop(heap)
            if cy == N-1 and cx == N-1:
                return curr_cost
            if curr_cost > cost[cy][cx][direction]:
                continue
                
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                # 범위 밖이거나, 도로를 건설할 수 없는 공간이면 탐색 X
                if not in_range(ny, nx) or board[ny][nx]:
                    continue
                # 다음 노드로 진행하는 방향이 현재까지 진행했던 방향과 같으면 일반 도로, 아니면 코너
                new_cost = curr_cost + 100 if direction in (i, -1) else curr_cost + 600
                if new_cost < cost[ny][nx][i]:
                    cost[ny][nx][i] = new_cost
                    heapq.heappush(heap, (cost[ny][nx][i], i, ny, nx))
        return
    
    N = len(board)
    heap = []
    heapq.heappush(heap, (0, -1, 0, 0))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    cost = [[[INF, INF, INF, INF] for _ in range(N)] for _ in range(N)]
    
    answer = dijkstra(heap)
    
    return answer