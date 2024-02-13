import sys

n,k = map(int,sys.stdin.readline().strip().split(' '))
seq = list(map(int,sys.stdin.readline().strip().split(" ")))

cnt = 0
multitap = []

for i in range(k) :
    print("\n turn of the plug number : %d ---------------------------"%(seq[i]))
    print(multitap)
    # 멀티탭이 겹치는 지,
    if seq[i] in multitap :
        print("Case 1")
        continue
    # 멀티탭에 빈 공간이 있는지.
    elif len(multitap) < n : # if multitab has empty line?
        multitap.append(seq[i])
        print("Case 2")
        continue
    # 1,2 둘 다 만족하지 못할 경우, 멀티탭을 빼는 판단.
    else :
        print("Case3")
        plug_idx = 0
        subp = 0
        for x in multitap :
            if x not in seq[i:] :
                subp = x
                break
            elif seq[i:].index(x) >= plug_idx:
                plug_idx = seq[i:].index(x)
                subp = x

        multitap.remove(x)
        multitap.append(seq[i])
        cnt += 1
print(cnt)