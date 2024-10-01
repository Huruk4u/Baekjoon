from collections import deque

def solution(N, M, sy, sx, ey, ex, K):
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
    
    def in_range(y, x):
        if (0 <= y < N) and (0 <= x < M):
            return True
        else:
            return False
    
    def promising(cy, cx, depth):
        det = abs(cy - ey) + abs(cx - ex)
        turn = K - depth
        if turn < det:
            return False
        if det - turn % 2 == 1:
            return False
        return True
    
    def tracking(queue):
        while queue:
            cy, cx, depth, path = queue.popleft()
            if cy == ey and cx == ex and depth == K:
                return path

            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if not in_range(ny, nx): continue
                if promising(ny, nx, depth + 1):
                    queue.append((ny, nx, depth+1, path+command[i]))
                    break
        
        return "impossible"
    
        # D, L, R, U 사전 순 접근
    dy, dx = [1, 0, 0, -1], [0, -1, 1, 0]
    command = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
    
    queue = deque([(sy, sx, 0, "")])
    visited = [[0] * M for _ in range(N)]
    
    return tracking(queue)