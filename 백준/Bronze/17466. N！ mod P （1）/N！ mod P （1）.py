import sys, math
input = sys.stdin.readline


if __name__ == '__main__':
    N, P = map(int, input().strip().split())

    temp = 1
    for i in range(2, N+1):
        temp *= i
        temp %= P

    print(temp)
    