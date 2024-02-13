import sys


def solve_range(length):
    max_n = length
    if length >= 10:
        max_n = 9 + (length - 9) // 2
    return max_n


def promising(x):
    global n_range

    if x > n_range or x < 1:
        return False
    else:
        return True


def backtracking(idx, ans, visited, ans_idx):
    global n_range
    print("=================== idx = %d =====================" % idx)
    # return
    if idx == len(num) and ans_idx == n_range:
        print(*ans)
        exit(0)

    x = int(num[idx])
    print("x = %d" % x)

    if not visited[x]:
        if promising(x):
            ans[ans_idx] = x
            print("ans = ", ans)
            visited[x] = True
            print("visited %d" % x)
            backtracking(idx+1, ans, visited, ans_idx+1)
            visited[x] = False

    if idx < len(num) - 1:
        print("---- exist ----")
        print("idx = %d, len(num)-1 = %d" % (idx, len(num) - 1))
        print("x = %d, num[idx+1] = %d" % (x, int(num[idx + 1])))
        x = x*10 + int(num[idx+1])
        print("x = %d" % x)
        if promising(x):
            ans[ans_idx] = x
            print("ans = ", ans)
            visited[x] = True
            print("visited %d" % x)
            backtracking(idx+2, ans, visited, ans_idx+1)
            visited[x] = False


if __name__ == '__main__':
    # input
    num = str(sys.stdin.readline().strip())

    n_range = solve_range(len(num))
    vst = [False] * (n_range+1)
    ans = [0] * n_range

    backtracking(0, ans, vst, 0)
