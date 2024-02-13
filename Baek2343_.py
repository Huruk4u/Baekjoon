import sys

n,m = map(int,sys.stdin.readline().strip().split())
lecture = list(map(int,sys.stdin.readline().strip().split()))

high = sum(lecture)
low = max(lecture) + 1

def finder(low,high):
    mid = (high+low)//2
    print("%d %d"%(low, high))
    print("mid = %d"%(mid))

    if (high-low) <= 1:
        print(low)
        return

    total_time = 0
    blueray_cnt = 0

    for i in range(n):
        if (total_time + lecture[i]) > mid:
            blueray_cnt += 1
            print("blueray = %d--------------------"%(total_time))
            total_time = lecture[i]
        else :
            total_time += lecture[i]
    if total_time :
        blueray_cnt += 1
    if blueray_cnt > m :
        finder(mid,high)
    else : # 조건 충족
        finder(low,mid)

finder(low, high)