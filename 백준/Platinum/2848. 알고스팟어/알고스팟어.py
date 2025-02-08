import sys
from collections import deque
input = sys.stdin.readline


def get_ord(char):
    return ord(char) - 97


def get_order(i, dtn):
    order = []
    prev_chr = 'A'
    for j in range(len(dtn)):
        if len(dtn[j]) <= i:
            continue
        if dtn[j][i] == prev_chr:
            continue
        prev_chr = dtn[j][i]
        order.append(prev_chr)

    return order


def get_relation(order):
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if graph[ord(order[i]) - 97][ord(order[j]) - 97]:
                continue
            graph[ord(order[i]) - 97][ord(order[j]) - 97] = True
            inDeg[ord(order[j]) - 97] += 1

    return


def get_graph(i, dtn):
    order = get_order(i, dtn)
    get_relation(order)
    if len(dtn) <= 1:
        return

    dictionary = [[] for _ in range(26)]
    for j in range(len(dtn)):
        if len(dtn[j]) <= i:
            continue
        dictionary[ord(dtn[j][i]) - 97].append(dtn[j])

    for c in order:
        used.add(c)
        get_graph(i+1, dictionary[ord(c) - 97])


def get_start_node(queue):
    cnt = 0
    for c in used:
        if not inDeg[get_ord(c)]:
            queue.append(c)
            inDeg[get_ord(c)] = -1
            cnt += 1

    if cnt > 1:
        return False
    else:
        return True


def tsort():
    global flag
    rtn = []
    queue = deque([])
    if not get_start_node(queue):
        flag = False

    while queue:
        curr = queue.popleft()
        curr_ord = get_ord(curr)
        rtn.append(curr)
        for next in range(26):
            if not graph[curr_ord][next]:
                continue
            inDeg[next] -= 1

        if not get_start_node(queue):
            flag = False

    return rtn


if __name__ == '__main__':
    N = int(input().strip())
    ipt = deque([str(input().strip()) for _ in range(N)])

    used = set()
    for idx in range(N):
        for c in ipt[idx]:
            used.add(c)

    dtn = []
    for i in range(N):
        s = ipt.popleft()
        dtn.append(s)
        for j in range(len(s)):
            if s[0:j] in ipt:
                print("!")
                exit()

    graph = [[False] * 26 for _ in range(26)]
    inDeg = [0 for _ in range(26)]
    flag = True

    get_graph(0, dtn)
    ans = tsort()
    if len(used) != len(ans):
        print("!")
    else:
        if flag:
            print(''.join(ans))
        else:
            print("?")
