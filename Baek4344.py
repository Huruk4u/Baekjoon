import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input().strip())

    for _ in range(T):
        # input
        ipt = list(map(int, input().strip().split()))
        N = ipt[0]

        # sum
        total = 0
        for i in range(1, len(ipt)):
            total += ipt[i]

        # average
        avr = total / N

        # rate
        cnt = 0
        for i in range(1, len(ipt)):
            if ipt[i] > avr:
                cnt += 1
        rate = (cnt / N) * 100

        print("{:.3f}%".format(rate))
