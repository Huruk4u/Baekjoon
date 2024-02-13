import sys

n = int(sys.stdin.readline().strip())

case = [0,1,1]

def pinary(i) :
    if i > n :
        return

    x = case[i-1] + case[i-2]
    case.append(x)
    pinary(i+1)

pinary(3)
print(case[n])