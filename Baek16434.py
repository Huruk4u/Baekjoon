# 22/07/26
import sys

n, curATK = map(int,sys.stdin.readline().strip().split())
res = 0
room = []
for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().strip().split())))

low = 0
high = int(2e17)

while low <= high:
    maxHP = (high+low)//2
    curHP = maxHP
    attack = curATK
    for i in range(n):
        # monster room
        if room[i][0] == 1:
            monATK = room[i][1]
            monHP = room[i][2]
            if (monHP%attack) == 0:
                turn = (monHP//attack)-1
            else :
                turn = monHP//attack
            curHP -= turn*monATK
            if curHP <= 0:
                break
        # portion room
        else:
            atk_up = room[i][1]
            hp_up = room[i][2]
            if (curHP + hp_up) > maxHP:
                curHP = maxHP
            else :
                curHP += hp_up
            attack += atk_up

    if curHP <= 0 :
        low = maxHP+1
    else:
        res = maxHP
        high = maxHP-1

print(res)