import sys

n,k = map(int,sys.stdin.readline().strip().split(' '))
seq = list(map(int,sys.stdin.readline().strip().split(" ")))

cnt = 0
multitap = []

for i in range(k) :
    if seq[i] in multitap :
        continue

    elif len(multitap) < n :
        multitap.append(seq[i])
        continue

    else :
        plug_idx = 0
        subp = 0
        for x in multitap :
            if x not in seq[i:] :
                subp = x
                break
            elif seq[i:].index(x) >= plug_idx:
                plug_idx = seq[i:].index(x)
                subp = x

        multitap.remove(subp)
        multitap.append(seq[i])
        cnt += 1

print(cnt)