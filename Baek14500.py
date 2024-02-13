import sys
input = sys.stdin.readline


# 좌우대칭
def symmetry(tetro):
    rtn = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rtn[i][3-j] = tetro[i][j]
    return rtn


# 회전
def rotate(tetro):
    rtn = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rtn[j][3-i] = tetro[i][j]

    return rtn


def in_range(di, dj, i, j):
    if (0 <= i + di < 4) and (0 <= j + dj < 4):
        return True
    else:
        return False

def tetro_in_range(i, j):
    if (0 <= i < N) and (0 <= j < M):
        return True
    else:
        return False


# 이동
def move(tetro):
    rtn = [[0] * 4 for _ in range(4)]
    for di in range(-3, 3):
        for dj in range(-3, 3):
            flag = True
            for i in range(4):
                for j in range(4):
                    if not flag:
                        break
                    if not in_range(di, dj, i, j) and tetro[i][j] == 1:
                        flag = False
                        break
                    else:
                        rtn[(i+di) % 4][(j+dj) % 4] = tetro[i][j]
            if flag:
                return rtn


if __name__ == '__main__':
    frag = []
    rot2 = []
    rot4 = []
    frag.append([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    rot2.append([[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    rot4.append([[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    sym_r4 = ([[1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]])
    sym_r2 = ([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])

    rot2.append(sym_r2)
    rot2.append(symmetry(sym_r2))

    rot4.append(sym_r4)
    rot4.append(symmetry(sym_r4))

    for r2 in rot2:
        frag.append(r2)
        frag.append(rotate(r2))
    for r4 in rot4:
        frag.append(r4)
        rt = r4
        for i in range(3):
            rt = rotate(rt)
            frag.append(rt)

    tetromino = []
    for t in frag:
        tetromino.append(move(t))

    N, M = map(int, input().strip().split())
    paper = [list(map(int, input().strip().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            print("========================")
            print("%d %d 기점" % (i, j))
            for tetro in tetromino:
                flag = True
                cnt = 0
                for c in range(4):
                    print(tetro[c])

                for ti in range(4):
                    for tj in range(4):
                        if not flag:
                            break
                        # print("i + ti = %d, j + tj = %d" % (i + ti, j + tj))
                        if tetro[ti][tj]:
                            if not tetro_in_range(i + ti, j + tj):
                                print("사이즈 안맞아서 진행 X")
                                flag = False
                                break
                            else:
                                cnt += paper[i+ti][j+tj]
                if flag:
                    print("취득점수 = %d" % cnt)
                    ans = max(ans, cnt)

    print(ans)