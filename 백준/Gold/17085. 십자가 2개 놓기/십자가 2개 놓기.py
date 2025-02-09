import sys
from pprint import pprint

input = sys.stdin.readline

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(y, x):
    if (0 <= y < N) and (0 <= x < M):
        return True
    else:
        return False


"""
    첫번째 십자가를 놓는다.
    cy, cx : 첫번째 십자가의 위치
    delta : 십자가 한 날개?의 길이 
"""
def first_cross_masking(cy, cx, delta):
    rtn = 0
    for i in range(4):
        ny, nx = cy + dy[i] * delta, cx + dx[i] * delta
        # 더이상 십자가를 확장할 수 없으면 종료
        if not in_range(ny, nx) or matrix[ny][nx] == '.':
            return 0

    # 십자가 마스킹
    for i in range(4):
        ny, nx = cy + dy[i] * delta, cx + dx[i] * delta
        matrix[ny][nx] = '*'

    rtn = max(rtn, find_second_cross(delta * 4 + 1))

    return rtn


"""
    두번째 십자가를 놓을 위치를 찾고, 두 십자가 크기의 곱 반환
"""
def find_second_cross(first_cross_size):
    rtn = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] != '#': continue
            delta = 0
            while True:
                second_cross_size = second_cross_masking(y, x, delta)
                # 만약 두번째 십자가를 더이상 확장할 수 없으면, break
                if second_cross_size:
                    rtn = max(rtn, first_cross_size * second_cross_size)
                else:
                    break
                delta += 1
    return rtn


"""
    두번째 십자가 놓을 수 있는지 체크
    cy, cx : 두번째 십자가의 중심 위치.
    delta : 두번째 십자가 한 쪽 날개?의 길이
    놓을 수 있으면 십자가의 크기를 반환, 놓을 수 없으면 0반환
"""
def second_cross_masking(cy, cx, delta):
    for i in range(4):
        ny, nx = cy + dy[i] * delta, cx + dx[i] * delta
        if not in_range(ny, nx) or matrix[ny][nx] != '#': return 0
    return delta * 4 + 1


"""
    첫번째 십자가를 지운다.
    cy, cx : 십자가의 중앙 위치
    delta : 십자가의 크기

"""
def erase_first_cross(cy, cx, delta):
    for dt in range(delta):
        for i in range(4):
            ny, nx = cy + dy[i] * dt, cx + dx[i] * dt
            matrix[ny][nx] = '#'
    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    matrix = [list(input().strip()) for _ in range(N)]

    """
        모든 경우의 수 탐색 : 
        - 한 좌표에서 만들 수 있는 최대 십자가의 수 : 7개
        - matrix 한 변의 최대 길이 <= 15
        - O((15 * 15 * 7)^2)
    """
    answer = 0
    for y in range(N):
        for x in range(M):
            # 십자가 생성할 수 없는 곳이면, continue
            if matrix[y][x] == '.': continue
            delta = 0
            while True:
                rtn = first_cross_masking(y, x, delta)
                if rtn:
                    answer = max(answer, rtn)
                    delta += 1
                else:
                    erase_first_cross(y, x, delta)
                    break

    print(answer)
