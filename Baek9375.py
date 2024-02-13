import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        wear = dict()
        for i in range(N):
            name, wearType = input().strip().split()
            if wearType in wear:
                wear[wearType] += 1
            else:
                wear[wearType] = 2

        rtn = 1
        for t in wear:
            rtn *= wear[t]

        print(rtn-1)
