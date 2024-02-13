import sys

n = int(sys.stdin.readline().strip())
listN = sorted(map(int,sys.stdin.readline().split(' ')))

m = int(sys.stdin.readline().strip())
listM = map(int,sys.stdin.readline().split(' '))

def finder(N,M,start,end):
    if start>end : return 0
    mid = (start+end)//2
    if N[mid]<M: start = mid+1
    elif M<N[mid]: end = mid-1
    else : return 1
    return finder(N,M,start,end)

for m in listM:
    start = 0
    end = len(listN)-1
    print(finder(listN,m,start,end))