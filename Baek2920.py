import sys

a,b,c,d,e,f,g,h = map(int,sys.stdin.readline().split(' '))
m = [a,b,c,d,e,f,g,h]

asp =0
desp = 0

for i in range(len(m)-1) :
    if m[i] + 1 == m[i+1] :
        asp +=1
    elif m[i] -1 == m[i+1] :
        desp +=1
    else : pass

if asp >= 7 : print("ascending")
elif desp >= 7 : print("descending")
else : print("mixed")