import sys


def bt(cnt):
    print("====================== cnt = %d =======================" % cnt)
    for y in range(10):
        for x in range(10):
            if paper[y][x] == 1:
                print("y = %d, x = %d" % (y, x))
                # 붙일 수 있는 종이의 최대 크기를 구함
                size_color = size(x, y)
                # 붙일 수 있는 종이가 큰 순서부터
                for s in range(size_color, 0, -1):
                    print("size of color paper = %d" % s)
                    if color[s]:
                        for i in range(y, y+s):
                            for j in range(x, x+s):
                                paper[i][j] = 0
                        color[s] -= 1
                        for i in range(10):
                            print(paper[i])
                        ans.add(bt(cnt+1))
                        print("cnt = %d" % cnt)
                        print("ans = ", ans)
                        color[s] += 1
                        for i in range(y, y+s):
                            for j in range(x, x+s):
                                paper[i][j] = 1
                        for i in range(10):
                            print(paper[i])
                if ans:
                    return min(ans)
                else:
                    return -1
    return cnt


def size(x, y):
    test_cnt = 0
    # x, y좌표 + 색종이의 크기는 10보다는 작아야 하고, 색종이의 크기는 5보다 작아야 함.
    for test_size in range(1, 6):
        print("x = %d, y = %d" % (x, y))
        print("test size = %d" % test_size)
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

    bt(0)

    print(ans)
