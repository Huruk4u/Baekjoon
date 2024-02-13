a = int(input())
num = a
cycle = 0

while True:
    cycle +=1
    num = ((num%10)*10) + (((num//10)+(num%10))%10)
    if num == a:
        break
print(cycle)