import sys

while True :
    tnf = 0
    n = int(sys.stdin.readline().strip())
    if n == 0 :
        break
    a = list(str(n))

    for i in range(len(a)//2):
        if int(a[i]) - int(a[-1 - i]) != 0:
            tnf = 1
            break
    if tnf == 0 :print("yes")
    else:
        print("no")