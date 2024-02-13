import heapq
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        K = int(input().strip())
        max_heap = []
        min_heap = []
        dict_num = dict()
        cnt = 0
        for k in range(K):
            token, n = map(str, input().strip().split())
            if token == 'D':
                if not cnt:
                    continue
                if n == '-1':   # 최솟값 삭제
                    while not dict_num[min_heap[0]] or min_heap[0] not in dict_num:
                        non = heapq.heappop(min_heap)
                        if non in dict_num:
                            del(dict_num[non])
                    dict_num[heapq.heappop(min_heap)] -= 1
                    cnt -= 1
                else:  # 최댓값 삭제
                    while not dict_num[-max_heap[0]] or -max_heap[0] not in dict_num:
                        non = -heapq.heappop(max_heap)
                        if non in dict_num:
                            del (dict_num[non])
                    dict_num[-heapq.heappop(max_heap)] -= 1
                    cnt -= 1
            else:
                heapq.heappush(max_heap, -int(n))
                heapq.heappush(min_heap, int(n))
                cnt += 1
                if int(n) in dict_num:
                    dict_num[int(n)] += 1
                else:
                    dict_num[int(n)] = 1
            print(min_heap, max_heap)
            print(dict_num)

        if cnt:
            while not dict_num[min_heap[0]] or min_heap[0] not in dict_num:
                heapq.heappop(min_heap)
            while not dict_num[-max_heap[0]] or -max_heap[0] not in dict_num:
                heapq.heappop(max_heap)
            print(max_heap, min_heap)
            print(dict_num)
            print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
        else:
            print("EMPTY")
