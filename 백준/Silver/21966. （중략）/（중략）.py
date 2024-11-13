import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    S = input().strip()
    if N <= 25:
        print(S)
    else:
        mid = S[11:-11]
        case3 = False
        for i in range(1, len(mid)-1):
            if mid[i] == '.':
                case3 = True

        if not case3:
            print("%s%s%s" % (S[:11], '...', S[-11:]))
        else:
            print("%s%s%s" % (S[:9], '......', S[-10:]))
