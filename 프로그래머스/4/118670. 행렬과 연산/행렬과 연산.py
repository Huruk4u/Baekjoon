from collections import deque


def solution(rc, operations):             
    N = len(rc)
    row = deque()
    for i in range(N):
        row.append(deque(rc[i]))
        
    left, right = deque(), deque()
    top, bottom = row[0], row[-1]
    for i in range(1, N-1):
        left.append(row[i].popleft())
        right.append(row[i].pop())
        
    left.appendleft(top.popleft())
    left.append(bottom.popleft())
    right.append(bottom.pop())
    right.appendleft(top.pop())
    
    for opr in operations:
        if opr == "ShiftRow":
            row.rotate()
            left.rotate()
            right.rotate()
            top, bottom = row[0], row[-1]
        else:
            top.appendleft(left.popleft())
            right.appendleft(top.pop())
            bottom.append(right.pop())
            left.append(bottom.popleft())
    
    # answer
    answer = [[] for _ in range(N)]
    
    for i in range(N):
        answer[i].append(left.popleft())
        while row[i]:
            answer[i].append(row[i].popleft())
        answer[i].append(right.popleft())
    
    return answer