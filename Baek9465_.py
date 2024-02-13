import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    n = int(sys.stdin.readline().strip())
    sticker = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(2)]
    for c in range(1,n):
        if c == 1:
            sticker[0][c] += sticker[1][c-1]
            sticker[1][c] += sticker[0][c-1]
        else :
            sticker[0][c] += max(sticker[1][c-1], sticker[1][c-2])
            sticker[1][c] += max(sticker[0][c-1], sticker[0][c-2])

    print(max(sticker[0][n-1], sticker[1][n-1]))
