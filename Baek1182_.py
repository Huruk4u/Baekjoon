# 22/09/22
import sys

n, s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0


def dfs(idx, n_sum):
    global cnt
    if idx >= n:
        return
    n_sum += arr[idx]
    if n_sum == s:
        cnt += 1

    dfs(idx+1, n_sum - arr[idx])
    dfs(idx+1, n_sum)


if __name__ == '__main__':
    dfs(0, 0)
    print(cnt)
