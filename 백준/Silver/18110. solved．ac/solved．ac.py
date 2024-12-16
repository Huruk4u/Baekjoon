import sys
input = sys.stdin.readline



def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


if __name__ == '__main__':
    N = int(input().strip())
    rate = sorted([int(input().strip()) for _ in range(N)])
    cut = custom_round(N * 0.15)

    rate = rate[cut:N-cut]

    if not N: print(0)
    else:
        print(custom_round(sum(rate) / len(rate)))
