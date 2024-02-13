import sys

n = int(sys.stdin.readline().strip())

stars = [["*" for x in range(n)] for y in range(n)]

v=n
cnt=0

while v != 1 :
    v/=3
    cnt+=1
print(cnt)
for cnt_ in range(cnt) :
    idx = [i for i in range(n) if (i//3 ** cnt_)%3 == 1]
    print(idx)
    for i in idx:
        for j in idx :
            stars[i][j] = " "

for i in stars :
    print("\n")
    for j in i :
        print(j,end="")