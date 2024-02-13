import sys
from collections import deque


def make_str(next_arr):
    string = ""
    for s in next_arr:
        string += s
    return string


def bfs(queue):
    curr, cnt = queue[0]
    curr_adr = make_str(curr)
    vst.add(curr_adr)
    while queue:
        curr, cnt = queue.popleft()
        print("============================================================")
        print("curr =>", curr)
        print("cnt = %d" % cnt)
        if curr == sorted_arr:
            return cnt

        for i in range(n-k+1):
            # make next_arr
            arr_slice = curr[i:i+k]
            arr_slice.reverse()
            next_arr = curr[:i] + arr_slice + curr[i+k:]
            next = make_str(next_arr)
            print("next = > ", next)

            if next not in vst:
                queue.append([next_arr, cnt+1])
                vst.add(next)

    return -1


if __name__ == '__main__':
    # input
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = list(map(str, sys.stdin.readline().strip().split()))
    # vst
    vst = {"".join(arr)}
    # sorted arr
    sorted_arr = sorted(arr)
    # queue
    q = deque()
    q.append([arr, 0])

    print(bfs(q))
