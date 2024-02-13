# 22/08/09
import sys
import collections

n,m = map(int,sys.stdin.readline().strip().split())
num_index = list(map(int,sys.stdin.readline().strip().split()))

# 일단 만들어놓는데 쓸지 안 쓸지 모름
q = collections.deque([i for i in range(1,n+1)])
cnt = 0

for num in num_index:
    print("----------%d"%(num))
    if q[0] == num:
        print("%d = %d"%(num,q[0]))
        q.popleft()
        continue
    # 2번 연산을 하는게 효율적인지, 3번 연산을 하는게 효율적인지 판단해야함.
    else :
        # num이 q 앞쪽 절반에 있으면 2번 연산
        print("len(q)//2 = %d"%(len(q)//2))
        print("q index = %d" % (q.index(num)))
        if q.index(num) <= len(q)//2:
            while q[0] != num :
                q.append(q[0])
                q.popleft()
                print("2 count --",q)
                cnt+=1
            q.popleft()
        else:
            while q[0] != num :
                q.appendleft(q[-1])
                q.pop()
                print("3 count --",q)
                cnt+=1
            q.popleft()

print(cnt)