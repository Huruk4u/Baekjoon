import sys

N = int(sys.stdin.readline().strip())
mlist = []

for _ in range(N):
    s, e = map(int,sys.stdin.readline().strip().split(' '))
    mlist.append([s,e])

mlist = sorted(mlist, key=lambda x:(x[1],x[0]))

end = ans = 0
for i in range(N):
    if end <= mlist[i][0]:
        ans += 1
        end = mlist[i][1]
print(ans)