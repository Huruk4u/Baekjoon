import sys, itertools, copy
from collections import deque
input = sys.stdin.readline


def woman_org(opr):
    return int(opr) - 1


def man_org(opr):
    return int(opr) - 6


def connect(bp, gp):
    boy_love = [-1, -1, -1, -1, -1]
    girl_love = [-1, -1, -1, -1, -1]
    flag = False
    while not flag:
        # 모두 짝을 찾았으면 break
        flag = True
        for i in range(5):
            # i번 여자가 짝을 맺지 못한 경우
            if girl_love[i] == -1:
                flag = False
                first = gp[i][0]
                rival = boy_love[first]
                # 우선순위의 남자가 이미 짝이 있는 경우
                if rival != -1:
                    # i번째 여자의 우선순위가 높으면 교체
                    if bp[first].index(i) < bp[first].index(rival):
                        boy_love[first] = i
                        girl_love[i] = first

                        girl_love[rival] = -1
                        gp[rival].popleft()
                    else:
                        # print("순위에서 밀렸으므로 우선순위 제거")
                        gp[i].popleft()
                else:
                    boy_love[first] = i
                    girl_love[i] = first

    return boy_love[0]


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        boy_priority = deque([tuple(map(man_org, input().strip().split())) for _ in range(4)])
        girl_priority = [deque(list(map(woman_org, input().strip().split()))) for _ in range(5)]

        case = list(itertools.permutations([0, 1, 2, 3, 4], 5))

        boy_priority.appendleft(case[0])
        pivot = connect(copy.deepcopy(boy_priority), copy.deepcopy(girl_priority))
        boy_priority.popleft()

        answer = False
        for i in range(1, len(case)):
            boy_priority.appendleft(case[i])
            rtn = connect(copy.deepcopy(boy_priority), copy.deepcopy(girl_priority))
            if rtn < pivot:
                answer = True
                break
            boy_priority.popleft()

        if answer:
            print("YES")
        else:
            print("NO")
