import sys
input = sys.stdin.readline


if __name__ == '__main__':
    MOD = 1234567891
    r = 31
    N = int(input().strip())
    string = input().strip()

    answer = 0
    for i in range(N):
        answer += (ord(string[i]) - ord('a') + 1) * (r ** i)

    print(answer % MOD)
