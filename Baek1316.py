import sys

T = int(sys.stdin.readline().strip())

res = 0

for t in range(T) :
    list1 = list(input())
    sortList = sorted(list1)
    overlapedList1 = 0
    overlapedSortList = 0

    for i in range(len(list1)) :
        if i == 0 :
            pass
        else :
            if list1[i] == list1[i-1] :
                overlapedList1 += 1
            else :
                pass
            if sortList[i] == sortList[i-1] :
                overlapedSortList += 1

    if overlapedList1 == overlapedSortList :
        res += 1
print(res)