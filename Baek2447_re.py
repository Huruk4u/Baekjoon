import sys

n = int(sys.stdin.readline().strip())

stars = [["*" for i in range(n)] for j in range(n)]

a=n
count =0

while a!=1 :
    a/=3
    count+=1

for x in range(count) :
    line = [a for a in range(n) if (a//(3 ** x))%3 == 1]
    for idx_1 in line :
        for idx_2 in line :
            stars[idx_1][idx_2] = " "

for i in stars :
    line = "".join(i)
    print(line)
