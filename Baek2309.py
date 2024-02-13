import sys

sh = sorted([int(sys.stdin.readline().strip()) for i in range(9)])

sumSh = sum(sh)
rem1 = rem2= 0
for i in sh:
    for j in sh:
        if i != j:
            if sumSh - (i + j) == 100:
                rem1 = i
                rem2 = j
sh.remove(rem1), sh.remove(rem2)
for x in sh:
    print(x)