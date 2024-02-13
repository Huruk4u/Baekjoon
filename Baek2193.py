import sys

n = int(sys.stdin.readline().strip())

# result
cnt = 0

def pinary(latest, i) :
    # len(arr), cnt to global variance
    global cnt, n
    # if n==counting index, cnt += 1 and return
    if n == i :
        cnt += 1
        return
    # three types cnt. 10,00,01
    if latest == 1 :
        pinary(0, i+1)
    else :
        pinary(0, i+1)
        pinary(1, i+1)

pinary(0,2)
print(cnt)