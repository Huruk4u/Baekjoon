import sys

up, down, height = map(int, sys.stdin.readline().split(' '))

day = (height-down) / (up-down)

if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)
