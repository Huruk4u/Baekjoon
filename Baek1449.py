import sys

n,l = map(int,sys.stdin.readline().strip().split(' '))

poh = sorted(map(int, sys.stdin.readline().strip().split(' ')))

ans = 1
start = poh[0]
end = start + l

for i in poh :
    if i <= end-0.5 : continue
    else :
        ans += 1
        start = i
        end = start + l

print(ans)