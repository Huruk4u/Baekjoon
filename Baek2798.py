from sys import stdin

n,cutLine = map(int, stdin.readline().split(' '))
c = stdin.readline().split(' ')
cardList = [int(i) for i in c]
resList = []

for fir in range(len(cardList)-2) :
    for sec in range(fir+1,len(cardList)-1) :
        for fin in range(sec+1,len(cardList)) :
            res = cardList[fir] + cardList[sec] + cardList[fin]
            if res <= cutLine : resList.append(res)

print(max(resList))