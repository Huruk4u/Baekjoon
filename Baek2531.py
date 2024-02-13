import sys
input = sys.stdin.readline


def sliding_window(s, e):
    rtn = 0
    while s != N:
        if e >= N:
            e %= N
        if s < e:
            window = sushi[s:e]
        else:
            window = sushi[s:] + sushi[:e]
        window = set(window)
        if c in window:
            rtn = max(rtn, len(window))
        else:
            rtn = max(rtn, len(window) + 1)

        s += 1
        e += 1

    return rtn


if __name__ == '__main__':
    N, d, k, c = map(int, input().strip().split())

    sushi = []
    for _ in range(N):
        sushi.append(int(input().strip()))

    print(sliding_window(0, k))
