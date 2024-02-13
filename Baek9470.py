import sys
from collections import deque
input = sys.stdin.readline


def start_node():
    rtn = deque([])
    for i in range(1, M+1):
        if not inDeg[i]:
            rtn.append(i)
            order[i] = 1

    return rtn


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        K, M, P = map(int, input().strip().split())

        graph = [[] for _ in range(M+1)]
        inDeg = [0 for _ in range(M+1)]
        order = [0 for _ in range(M + 1)]
        recentOrder = [0 for _ in range(M+1)]

        for _ in range(P):
            a, b = map(int, input().strip().split())
            graph[a].append(b)
            inDeg[b] += 1

        queue = start_node()
        while queue:
            curr = queue.popleft()
            print("=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("현재 노드 번호 = %d, %d" % (curr, order[curr]))
            print("다음 노드 목록", graph[curr])
            for next in graph[curr]:
                inDeg[next] -= 1
                if recentOrder[next] == order[curr]:  # 다음 노드를 방문했던 노드의 순서가 현재 노드의 순서와 동일한 경우
                    order[next] = max(order[curr] + 1, order[next])
                else:
                    order[next] = max(order[next], order[curr])
                    recentOrder[next] = max(order[curr], recentOrder[next])
                # 다음 순서가 될 노드 처리, 들어오는 노드 중 strahelr의 값이 같은 것이 1개인지 2개인지 체크해야 함.
                if not inDeg[next]:
                    queue.append(next)

        print(K, order[M])
