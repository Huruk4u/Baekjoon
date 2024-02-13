import sys

input = sys.stdin.readline


def mono():
    global k
    for i in range(1, 9):
        dp[i].add(int(str(k) * i))
        for j in range(1, i):
            for a in dp[i - j]:
                for b in dp[j]:
                    dp[i].add(a + b)
                    dp[i].add(abs(a - b))
                    dp[i].add(a * b)
                    if a != 0 and b != 0:
                        dp[i].add(a // b)


if __name__ == '__main__':
    k = int(input().strip())
    n = int(input().strip())

    dp = [set() for _ in range(9)]
    mono()

    for _ in range(n):
        x = int(input().strip())
        flag = False
        for t in range(1, 9):
            if x in dp[t]:
                flag = True
                print(t)
                break
        if not flag:
            print("NO")
