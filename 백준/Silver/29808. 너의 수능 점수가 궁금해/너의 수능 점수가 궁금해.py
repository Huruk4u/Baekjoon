import sys
input = sys.stdin.readline


if __name__ == '__main__':
    S = int(input().strip())
    case = []
    
    if S % 4763:
        print(0)
    else:
        S //= 4763
        for x in range(201):
            for y in range(201):
                if x * 508 + y * 212 == S or x * 508 + y * 305 == S or x * 108 + y * 212 == S or x * 108 + y * 305 == S:
                    case.append((x, y))

        print(len(case))
        for i in case:
            print(*i)
