import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().strip().split())

    rtn = 1
    div = 1
    for i in range(K):
        rtn *= (N-i)
        div *= (K-i)

    print(rtn//div)