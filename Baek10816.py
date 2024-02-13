import sys
input = sys.stdin.readline


if __name__ == '__main__':
    # input
    N = int(input().strip())
    ipt = list(map(int, input().strip().split()))
    M = int(input().strip())
    query = list(map(int, input().strip().split()))

    card = {}
    for i in range(N):
        if ipt[i] in card:
            card[ipt[i]] += 1
        else:
            card[ipt[i]] = 1

    for i in range(M):
        if query[i] in card:
            if i == M-1:
                print('%d' % card[query[i]])
            else:
                print('%d' % card[query[i]], end=' ')
        else:
            if i == M-1:
                print('0')
            else:
                print('0', end=' ')
