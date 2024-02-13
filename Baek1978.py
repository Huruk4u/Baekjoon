T = int(input())
a = list(map(int,input().split(' ')))
res = 0
if T == len(a) :
    for n in a :
        count = 0
        for i in range(1,n+1) :
            if n%i == 0 :
                count += 1
        if count == 2 :
            res +=1
print(res)