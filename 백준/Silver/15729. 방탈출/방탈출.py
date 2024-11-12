import sys
input = sys.stdin.readline


def click(idx):
    for i in range(3):
        if idx+i >= N:
            return
        else:
            button[idx+i] = not button[idx+i]


if __name__ == '__main__':
    N = int(input().strip())
    button = list(map(int, input().strip().split()))

    cnt = 0
    for i in range(N):
        if button[i]:
            click(i)
            cnt += 1

    print(cnt)
