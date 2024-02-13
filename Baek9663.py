# 22/09/29
import sys

# 대각 이동 delta
dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]


def diagonal(curr_x, curr_y, atk):
    for i in range(4):
        next_x = curr_x + dx[i]
        next_y = curr_y + dy[i]
        while True:
            if 0 > next_x or next_x >= n or 0 > next_y or next_y >= n:
                break
            atk[next_x][next_y] = True
            next_x += dx[i]
            next_y += dy[i]


def backtracking(curr_x, curr_y, atk, n_queen, q):
    print("queen on %d %d" % (curr_x, curr_y))
    global cnt
    n_queen += 1
    if n_queen == n:
        cnt += 1
        print("cnt + 1")
        return

    new_atk = atk
    for k in range(n):
        new_atk[curr_x][k] = True
        new_atk[k][curr_y] = True

    diagonal(curr_x, curr_y, new_atk)

    for i in range(n):
        for j in range(n):
            if not atk[i][j] and not queen[i][j]:
                print("atk ->", atk)
                queen[i][j] = True
                q.append((i, j))
                print(q)
                backtracking(i, j, new_atk, n_queen, q)
                queen[i][j] = False
                q.pop()
                for k in range(n):
                    atk


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    cnt = 0

    for y in range(n):
        for x in range(n):
            print("=======================================================================================")
            attack = [[False] * n for _ in range(n)]
            queen = [[False] * n for _ in range(n)]
            q = []
            attack[y][x] = True
            backtracking(x, y, attack, 1, q)

    print(cnt)

