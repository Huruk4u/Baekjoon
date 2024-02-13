import sys


def bt(cnt):
    for y in range(10):
        for x in range(10):
            if paper[y][x] == 1:
                # 붙일 수 있는 종이의 최대 크기를 구함
                size_color = size(x, y)
                for s in range(size_color, 0, -1):
                    if color[s]:
                        for i in range(y, y+s):
                            for j in range(x, x+s):
                                paper[i][j] = 0
                        color[s] -= 1
                        ans.add(bt(cnt+1))
                        color[s] += 1
                        for i in range(y, y+s):
                            for j in range(x, x+s):
                                paper[i][j] = 1
                if ans:
                    return min(ans)
                else:
                    return -1
    return cnt


def size(x, y):
    test_cnt = 0
    for test_size in range(1, 6):
        if (x + test_size < 11) and (y + test_size < 11):
            for i in range(test_size):
                for j in range(test_size):
                    if paper[y+i][x+j] == 0:
                        return test_cnt
            test_cnt += 1
    return test_cnt


if __name__ == '__main__':
    paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(10)]
    color = [0, 5, 5, 5, 5, 5]
    ans = set()

    ans.add(bt(0))

    if min(ans) == -1:
        ans.remove(-1)
    if ans:
        print(min(ans))
    else:
        print(-1)
