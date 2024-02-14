import sys
input = sys.stdin.readline


# 8!
def backtracking(arr):
    if len(arr) == M:
        print(*arr)
        return
    prev = 0
    for i in range(N):
        if is_used[i] or prev == number[i]:
            continue
        is_used[i] = True
        prev = number[i]
        backtracking(arr + [number[i]])
        is_used[i] = False

    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())
    number = sorted(list(map(int, input().strip().split())))
    is_used = [False] * N

    prev = 0
    for i in range(N):
        if prev == number[i]:
            continue
        is_used[i] = True
        prev = number[i]
        backtracking([number[i]])
        is_used[i] = False
