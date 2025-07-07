import sys
input = sys.stdin.readline

answer = sys.maxsize

def dfs(d1, d2, depth, move):
    global answer

    if depth == M:
        answer = min(answer, move)
        return

    temp1 = abs(d1 - show[depth])
    temp2 = abs(d2 - show[depth])

    dfs(show[depth], d2, depth+1, move + temp1)
    dfs(d1, show[depth], depth+1, move + temp2)


if __name__ == '__main__':
    N = int(input().strip())
    d1, d2 = map(int, input().strip().split())

    M = int(input().strip())
    show = [int(input().strip()) for i in range(M)]

    dfs(d1, d2, 0, 0)

    print(answer)