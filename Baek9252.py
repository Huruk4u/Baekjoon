import sys
input = sys.stdin.readline


if __name__ == '__main__':
    s1 = [""] + list(input().strip())
    s2 = [""] + list(input().strip())
    lcs = [[""] * len(s2) for _ in range(len(s1))]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                lcs[i][j] = lcs[i-1][j-1] + s1[i]
            else:
                if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                    lcs[i][j] = lcs[i-1][j]
                else:
                    lcs[i][j] = lcs[i][j-1]

    print("%d\n%s" % (len(lcs[-1][-1]), lcs[-1][-1]))
