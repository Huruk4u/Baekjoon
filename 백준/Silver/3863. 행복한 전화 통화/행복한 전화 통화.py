import sys
input = sys.stdin.readline


if __name__ == '__main__':
    while True:
        N, M = map(int, input().strip().split())
        if N == 0 and M == 0:
            break
        call = []
        for _ in range(N):
            g1, g2, start, duration = map(int, input().strip().split())
            call.append((start, start + duration))

        for _ in range(M):
            start, end = map(int, input().strip().split())
            end = start + end
            rtn = 0
            for i in range(len(call)):
                if end <= call[i][0] or start >= call[i][1]:
                    continue
                rtn += 1
            print(rtn)
