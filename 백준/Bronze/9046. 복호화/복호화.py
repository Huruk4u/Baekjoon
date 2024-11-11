import sys
input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        ipt = input().strip()
        cnt = [0] * 26
        for i in range(len(ipt)):
            if ipt[i] == ' ': continue
            cnt[ord(ipt[i]) - ord('a')] += 1

        if cnt.count(max(cnt)) >= 2:
            print("?")
        else:
            print(chr(cnt.index(max(cnt)) + ord('a')))
