import sys

n = int(sys.stdin.readline().strip())
listN = []
for i in range(n) :
    s = int(sys.stdin.readline().strip())
    listN.append(s)

srtList = sorted(listN)
count = 1

# 산술 평균
ave = sum(listN)/n
print(round(ave))
# 중앙값
cenindex = int(n/2)
cen = srtList[cenindex]
print(cen)
# 최빈값
cntList = []
for j in range(len(srtList)) :
        if j == 0 :
            pass
        if srtList[j] == srtList[j-1]:
            count+=1
            cntList.append(count)
        else :
            count=1
            cntList.append(count)
maxco = cntList.count(max(cntList))
manList = []
if maxco >= 2:
    for x in range(len(cntList)):
        if cntList[x] == max(cntList) : manList.append(srtList[x])
    man = manList[1]
    print(man)
else :
    man = srtList[cntList.index(max(cntList))]
    print(man)
# 범위
ran = max(listN) - min(listN)
print(ran)