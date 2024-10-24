import sys
input = sys.stdin.readline

# 하, 우, 상, 좌
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]


def in_range(y, x):
    if (0 <= y < R) and (0 <= x < C):
        return True
    else:
        return False


if __name__ == '__main__':
    C, R = map(int, input().strip().split())
    cust = int(input().strip())
    matrix = [[0] * C for _ in range(R)]

    cy, cx = 0, 0
    cursor = 0
    flag = False
    for i in range(1, cust):
        matrix[cy][cx] = i
        ny, nx = cy + dy[cursor], cx + dx[cursor]
        if not in_range(ny, nx) or matrix[ny][nx]:
            cursor = (cursor + 1) % 4
            ny, nx = cy + dy[cursor], cx + dx[cursor]
            if not in_range(ny, nx) or matrix[ny][nx]:
                flag = True
                break
        cy, cx = ny, nx

    if flag: print(0)
    else: print(cx+1, cy+1)
