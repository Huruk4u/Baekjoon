import sys
n = int(sys.stdin.readline().strip())
sbj = [list(map(int,sys.stdin.readline().strip().split(' '))) for i in range(n)]
total = 0
for i in range(n,0,-1) :
    subject = []
    sbjW = 0
    for s in sbj :
        if s[0] >= i and s[1] >= sbjW :
            sbjW = s[1]
            subject = s
    if sbjW != 0 :
        total += sbjW
        sbj.remove(subject)
print(total)