import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())

    arr = [0] * 10001
    for _ in range(N):
        ipt = int(input().strip())
        arr[ipt] += 1

    for i in range(1, 10001):
        if arr[i]:
            for j in range(arr[i]):
                print(i)
