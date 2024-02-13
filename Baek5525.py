import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input().strip())
    M = int(input().strip())
    S = str(input().strip())
    stack = []
    need_1 = True
    rtn = 0
    for i in range(M):
        print("현재 위치 = %s, need_1? = %d" % (S[i], need_1))
        if S[i] == 'I' and need_1:
            stack.append(S[i])
            need_1 = False
        elif S[i] == 'O' and not need_1:
            stack.append(S[i])
            need_1 = True
        else:
            if not stack:
                continue
            print("스택 쌓기 중지")
            if stack[-1] == 'O':
                stack.pop()
            print("현재 스택 상태", stack)
            if len(stack) >= N + (N + 1):
                pn = len(stack)//2
                print("%d 에게 %d - %d + %d 가산" % (rtn, pn, N, 1))
                rtn += (pn - N + 1)
            stack = []
            if S[i] == 'I':
                stack.append(S[i])
                need_1 = False
            else:
                need_1 = True
        print("stack", stack)
    if stack:
        if stack[-1] == 'O':
            stack.pop()
        if len(stack) >= (2 * N) + 1:
            rtn += (len(stack) // 2) - N + 1
    print(rtn)