import sys
input = sys.stdin.readline


if __name__ == '__main__':
    target = str(input().strip())
    N = int(input().strip())
    if N:
        btnBreak = list(map(str, input().strip().split()))
    else:
        btnBreak = []

    low_case = 10000000000
    high_case = 10000000000
    brute_case = abs(int(target) - 100)
    # target ~ 0
    for n in range(int(target), -1, -1):
        flag = True
        for s in btnBreak:  # 9
            if s in str(n): # 6
                flag = False
                break
        if flag:
            low_case = n
            break

    # target + 1 ~ 1,000,000
    for n in range(int(target) + 1, 1000001):
        flag = True
        for s in btnBreak:
            if s in str(n):
                flag = False
                break
        if flag:
            high_case = n
            break

    low_case = len(str(low_case)) + (abs(int(target) - low_case))
    high_case = len(str(high_case)) + (high_case - int(target))

    print(min(low_case, high_case, brute_case))
