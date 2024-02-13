import sys

a = int(sys.stdin.readline().strip())

if a%4 != 0 : # a가 4의 배수가 아닐 때,
        print(0)
elif a%100 == 0 : # a가 100의 배수일 때,
    if a%400 == 0 : # a가 400의 배수라면
        print(1)
    else : print(0)
else : print(1)