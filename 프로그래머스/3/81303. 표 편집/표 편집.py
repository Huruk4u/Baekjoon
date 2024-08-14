def solution(N, K, commands):
    
    def up(cursor, X):
        for i in range(X):
            cursor = next_node[cursor][0]
        return cursor

    def down(cursor, X):
        for i in range(X):
            cursor = next_node[cursor][1]
        return cursor

    answer = ['O' for _ in range(N)]

    cursor, stack = K, []  # 현재 위치, stack[top]: 가장 최근 삭제된 노드 정보
    next_node = [[i - 1, i + 1] for i in range(N)]  # nextNode[i]: curr노드의 전후 연결된 노드
    next_node[0], next_node[N - 1] = [None, 1], [N - 2, None]
    for cmd in commands:
        if cmd == 'C':  # 삭제 명령
            currNum, left, right = cursor, next_node[cursor][0], next_node[cursor][1]
            stack.append((currNum, left, right))
            if left is not None: next_node[left][1] = right
            if right is not None: next_node[right][0] = left

            answer[cursor] = 'X'
            if right is None: cursor = left
            else: cursor = right

        elif cmd == 'Z':  # 복구 명령
            curr, left, right = stack.pop()
            if left is not None: next_node[left][1] = curr
            if right is not None: next_node[right][0] = curr

            answer[curr] = 'O'

        else:  # 이동 명령
            direct, X = cmd.split()
            if direct == 'U':
                cursor = up(cursor, int(X))
            else:
                cursor = down(cursor, int(X))

    return "".join(answer)