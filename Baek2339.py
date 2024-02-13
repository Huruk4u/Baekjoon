import sys
input = sys.stdin.readline


# 이물질의 존재 여부 확인
def exist_imp(loc_a, loc_b, loc_i):
    y1, x1 = loc_a
    y2, x2 = loc_b
    yi, xi = loc_i
    if (x1 <= xi < x2) and (y1 <= yi < y2):
        print("%d <= %d < %d and %d <= %d < %d" % (x1, xi, x2, y1, yi, y2))
        return True
    else:
        return False


# 석판 내의 보석 개수 확인
def jewel_n(loc_a, loc_b):
    y1, x1 = loc_a
    y2, x2 = loc_b

    rtn = 0
    for yj, xj in loc_jewel:
        if (x1 <= xj < x2) and (y1 <= yj < y2):
           rtn += 1
    print("보석의 개수 : %d" % rtn)
    return rtn


# 해당 이물질을 자를 수 있는지 여부 체크
def cut_able(loc_a, loc_b, loc_i, vertical):
    y1, x1 = loc_a
    y2, x2 = loc_b
    yi, xi = loc_i

    if vertical:  # 세로 방향 자르기
        for yj, xj in loc_jewel:
            if xi == xj and (y1 <= yj < y2):
                print("동일 선상 %d %d에 보석이 존재하므로 자를 수 없음" % (xj, yj))
                return False
            else:
                return True
    else:
        for yj, xj in loc_jewel:
            if yi == yj and (x1 <= xj < x2):
                print("동일 선상 %d %d에 보석이 존재하므로 자를 수 없음" % (xj, yj))
                return False
            else:
                return True


def dq(loc_a, loc_b, vertical):
    print("==================================================")
    y1, x1 = loc_a
    y2, x2 = loc_b
    print("현재 석판은 (%d, %d)부터 (%d, %d)까지" % (x1, y1, x2, y2))
    not_imp = True
    if (x2 - x1) < 1 or (y2 - y1) < 1:
        print("석판 범위 존재하지 않음")
        return 1
    rtn = 0
    for loc in loc_imp:
        yi, xi = loc
        print(loc_a, loc_b, loc)
        if exist_imp(loc_a, loc_b, loc):  # 현재 석판에 이물질이 존재하는 경우
            print("%d %d에 이물질이 존재함" % (xi, yi))
            not_imp = False
            if cut_able(loc_a, loc_b, loc, vertical):
                if vertical:
                    if dq((y1, x1), (y2, xi), False) and dq((y1, xi+1), (y2, x2), False):
                        rtn += 1
                        return rtn
                else:
                    if dq((y1, x1), (yi, x2), True) and dq((yi+1, x1), (y2, x2), True):
                        rtn += 1
                        return rtn

    if not_imp:
        print("이물질 존재하지 않음")
        if jewel_n(loc_a, loc_b) == 1:
            print("모든 조건을 만족함")
            return 1
        else:
            print("조건 불만족")
            return 0
    else:
        print("조건 불만족")
        return 0


if __name__ == '__main__':
    N = int(input().strip())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    loc_jewel = []
    loc_imp = []
    # 20 * 20
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                loc_imp.append((i, j))
            elif matrix[i][j] == 2:
                loc_jewel.append((i, j))

    print(dq((0, 0), (N, N), True))
    print(dq((0, 0), (N, N), False))