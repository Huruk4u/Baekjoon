import sys


def backtracking(row, queen_pos):
    global ans, n
    print(row)
    # if 마지막 행+1에 도달했다면, ans+1
    if row == n+1:
        ans += 1
    else:
        for j in range(1, n+1):
            queen_pos[row] = j
            if promising(row, queen_pos):
                backtracking(row+1, queen_pos)


def promising(row, queen_pos):
    print("=========promising==========\nrow = %d" % row)
    print(queen_pos)
    # 다른 퀸과 수직관계 여부 판단
    flag = True
    for r in range(1, row):
        print("r queen = %d, row queen = %d" % (queen_pos[row], queen_pos[r]))
        if queen_pos[row] == queen_pos[r]:
            flag = False
    # 다른 퀸과 대각 관계 여부 판단
        print("queen_pos row - queen pos r = %d" % (abs(queen_pos[row]- queen_pos[r])))
        if abs(queen_pos[row] - queen_pos[r]) == (row - r):
            flag = False
    return flag


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    queen_pos = [0] * (n+1)
    ans = 0

    backtracking(1, queen_pos)

    print(ans)