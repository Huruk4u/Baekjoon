import sys

T = int(sys.stdin.readline().strip())

for i in range(T) :
    floor, ho, n = map(int, input().split(' '))
    guestF = 0
    guestHo = 1
    if n%floor== 0 :
        guestF = floor
    else :
        guestF = n%floor

    if n//floor >= 1 :
        if n%floor == 0 :
            guestHo += n//floor-1
        else :
            guestHo += n//floor

    print((guestF*100) + guestHo)