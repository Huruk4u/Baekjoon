import sys
input = sys.stdin.readline


# 8!
def backtracking(arr):
    if len(arr) == M:
        # log(N!)
        if tuple(arr) not in rtn:
            rtn.add(tuple(arr))
        return

    for i in range(N):
        if is_used[i]:
            continue
        is_used[i] = True
        backtracking(arr + [number[i]])
        is_used[i] = False

    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    number = sorted(list(map(int, input().strip().split())))
    is_used = [False] * N
    rtn = set()

    for i in range(N):
        is_used[i] = True
        backtracking([number[i]])
        is_used[i] = False

    rtn = sorted(rtn)
    for r in rtn:
        print(*r)

