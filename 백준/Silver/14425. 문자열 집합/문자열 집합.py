import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().strip().split())

    S, cnt = set(), 0
    for _ in range(N):
        S.add(input().strip())
    for _ in range(M):
        if input().strip() in S:
            cnt += 1
    
    print(cnt)