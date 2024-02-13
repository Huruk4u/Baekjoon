import sys


def solve_range(length):
    max_n = length
    if length > 10:
        max_n = 9 + (length - 9) // 2
    return max_n


def backtracking(idx, ans_idx):
    global finish, ans

    if idx == len(num) and ans_idx == n_range:
        print(*ans)
        exit(0)

    x1 = int(num[idx])

    if not vst[x1]:
        ans[ans_idx] = x1
        vst[x1] = True
        backtracking(idx+1, ans_idx+1)
        vst[x1] = False
    if idx+1 < len(num):
        x2 = x1*10 + int(num[idx+1])
        if x2 < n_range + 1 and not vst[x2]:
            ans[ans_idx] = x2
            vst[x2] = True
            backtracking(idx+2, ans_idx+1)
            vst[x2] = False


if __name__ == '__main__':
    num = sys.stdin.readline().strip()

    n_range = solve_range(len(num))

    vst = [0 for _ in range(n_range+1)]
    ans = [0 for _ in range(n_range)]

    backtracking(0, 0)
