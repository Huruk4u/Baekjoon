# 22/08/25
import sys

n,p = map(int,sys.stdin.readline().strip().split())
melody = []
for _ in range(n):
    l, f = map(int, sys.stdin.readline().strip().split())
    melody.append([l, f])

guitar = []
for _ in range(6):
    guitar.append([0]) # 굳이 0을 넣어놓은 이유는 17번 line의 연산을 위해서

stack = []; cnt = 0
for line, fret in melody:
    print("======================\nline = %d fret = %d"%(line,fret))
    print("guitar line stack[-1] = %d"%(guitar[line-1][-1]))
    # 누를 fret이 이미 누르고 있는 fret보다 높다면
    if fret > guitar[line-1][-1]:
        print("1번 연산, %d번 줄에 %d추가"%(line,fret))
        guitar[line-1].append(fret)
        print(guitar[line-1])
        cnt += 1
    # 그게 아닌 경우, 누를 fret이 해당 라인의 줄보다 낮은 경우
    else:
        # 해당 라인에 뭔가를 누르고 있으면
        if guitar[line-1]:
            print("해당 줄에 뭔갈 누르고 있음")
            # 동일하거나 낮은 프렛이 나올 때까지 계속 pop을 함
            while guitar[line-1][-1] > fret:
                guitar[line-1].pop()
                print("pop",guitar[line-1])
                cnt += 1
        if guitar[line-1][-1] == fret:
            print("3번 연산, 쓰고있는 줄이 동일함")
            continue
        else:
            print("2번 연산, %d번 줄에 %d추가" % (line, fret))
            guitar[line-1].append(fret)
            print(guitar)
            cnt += 1

print(cnt)