import sys

m = int(sys.stdin.readline().strip())
state = 0

for _ in range(m):
    ipt = sys.stdin.readline().strip().split()
    if ipt[0] == "all":
        state = (1 << 21) - 1
        continue
    elif ipt[0] == "empty":
        state = 0
        continue
    else:
        command = ipt[0]
        x = int(ipt[1])
        if command == "add":
            state |= (1 << x)
        elif command == "remove":
            state &= ~(1 << x)
        elif command == "check":
            if state & (1 << x):
                print(1)
            else:
                print(0)
        elif command == "toggle":
            state ^= (1 << x)
