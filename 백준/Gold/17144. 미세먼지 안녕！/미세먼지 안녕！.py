import sys
from pprint import pprint

input = sys.stdin.readline
dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]


def in_range(y, x):
    if (0 <= y < R) and (0 <= x < C):
        return True
    else:
        return False


def spread(dust):
    new_dust = [[0 for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            spread_cnt = 0
            if not dust[y][x] or dust[y][x] == -1:
                continue
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if in_range(ny, nx) and dust[ny][nx] != -1:
                    new_dust[ny][nx] += int(dust[y][x] / 5)
                    spread_cnt += 1
            dust[y][x] -= int(dust[y][x] / 5) * spread_cnt

    for y in range(R):
        for x in range(C):
            new_dust[y][x] += dust[y][x]

    return new_dust


def cleaning(up):
    if up:
        cy, cx = cln_locate, 1
    else:
        cy, cx = cln_locate+1, 1

    temp, wind = 0, 0
    while True:
        ny, nx = cy + dy[wind], cx + dx[wind]
        if not in_range(ny, nx):
            # 위쪽 청정기면 정방향, 아래쪽 청정기면 역방향
            if up:
                wind = (wind + 1) % 4
            else:
                wind = (wind - 1) % 4
            continue
        if up and cy == cln_locate and cx == 0:
            break
        elif not up and cy == cln_locate + 1 and cx == 0:
            break

        dust[cy][cx], temp = temp, dust[cy][cx]
        cy, cx = ny, nx
    return


if __name__ == '__main__':
    R, C, T = map(int, input().strip().split())
    dust = [list(map(int, input().strip().split())) for _ in range(R)]

    cln_locate = 0
    for i in range(R):
        if dust[i][0] == -1:
            cln_locate = i
            break

    for _ in range(T):
        dust = spread(dust)
        cleaning(True)
        cleaning(False)


    answer = 0
    for r in range(R):
        for c in range(C):
            if dust[r][c] == -1:
                continue
            answer += dust[r][c]
    print(answer)


