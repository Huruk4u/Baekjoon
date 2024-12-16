import sys
input = sys.stdin.readline


if __name__ == '__main__':
    MOD = 1234567891

    a = [i for i in range(1, 27)]
    N = int(input().strip())
    string = input().strip()

    r, answer = 1, 0
    for i in range(N):
        answer += (a[ord(string[i]) - ord('a')] * r) % MOD
        r *= 31

    print(answer)
