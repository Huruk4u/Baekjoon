import sys

while True :
    num = list(map(int,sys.stdin.readline().split(' ')))
    if sum(num) == 0 :
        break
    z = max(num)
    num.remove(max(num))

    if (num[0]**2)+(num[1]**2) == z**2 :
        print("right")
    else : print("wrong")