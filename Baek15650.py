import sys
input = sys.stdin.readline


def backtracking(arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(arr[-1], N+1):
        if i in arr:
            continue
        backtracking(arr + [i])

    return


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    for i in range(1, N+1):
        backtracking([i])
