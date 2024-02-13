import sys

input = sys.stdin.readline


def two_pointer(s, e):
    global flag

    while True:
        dist = (e ** 2) - (s ** 2)
        if dist < G:
            e += 1
        elif dist == G:
            flag = True
            print(e)
            e += 1
        else:  # dist > G
            if s == e - 1:
                return
            s += 1


if __name__ == '__main__':
    G = int(input().strip())

    flag = False
    two_pointer(1, 1)

    if not flag:
        print(-1)
