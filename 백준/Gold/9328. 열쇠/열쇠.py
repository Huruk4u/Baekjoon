import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    if (0 <= y < N) and (0 <= x < M):
        return True
    else:
        return False


def bfs(queue):
    rtn = 0
    non_find = dict()
    while queue:
        cy, cx = queue.popleft()
        # 현재 노드가 door에 해당하는 경우
        if 'A' <= matrix[cy][cx] <= 'Z' and not find_key[ord(matrix[cy][cx]) - ord('A')]:
            if matrix[cy][cx] not in non_find:
                non_find[matrix[cy][cx]] = deque([(cy, cx)])
            else:
                non_find[matrix[cy][cx]].append((cy, cx))
            continue

        # 방문 처리
        if visited[cy][cx]:
            continue
        visited[cy][cx] = True

        # 방문한 현재 노드가 문서인 경우
        if matrix[cy][cx] == '$':
            rtn += 1

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            # 다음 단계로 진행할 수 없는 경우
            if not in_range(ny, nx) or visited[ny][nx]: continue
            if matrix[ny][nx] == '*': continue

            # 다음 노드가 key에 해당하는 경우
            if 'a' <= matrix[ny][nx] <= 'z':
                find_key[ord(matrix[ny][nx]) - ord('a')] = True
                # 이미 방문한 door 중에 key에 맞는 door가 존재하는 경우
                if matrix[ny][nx].upper() in non_find:
                    while non_find[matrix[ny][nx].upper()]:
                        y, x = non_find[matrix[ny][nx].upper()].popleft()
                        queue.append((y, x))

            queue.append((ny, nx))

    return rtn


def enter(y, x):
    if matrix[y][x] in ('.', '$') or 'A' <= matrix[y][x] <= 'Z':
        return True
    elif 'a' <= matrix[y][x] <= 'z':
        find_key[ord(matrix[y][x]) - ord('a')] = True
        return True
    else:
        return False


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        matrix = [list(input().strip()) for _ in range(N)]

        # 키 등록
        keys = input().strip()
        find_key = [False] * 26
        if keys != '0':
            for key in keys:
                find_key[ord(key) - ord('a')] = True
        visited = [[False] * M for _ in range(N)]

        # 벽으로 들어갈 수 있는 입구 찾기
        queue = deque()
        for i in range(N):
            if enter(i, 0):
                queue.append((i, 0))
            if enter(i, M-1):
                queue.append((i, M-1))
        for j in range(M):
            if enter(0, j):
                queue.append((0, j))
            if enter(N-1, j):
                queue.append((N-1, j))

        answer = bfs(queue)
        print(answer)
