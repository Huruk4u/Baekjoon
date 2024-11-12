import sys
sys.setrecursionlimit(100000001)


def solution(K, room_number):
    def find(number):
        if number in used:
            next_room = find(next[number])
            next[number] = next_room
            return next[number]
        else:
            return number

    used = set()
    next = dict()
    answer = []
    for i in range(len(room_number)):
        # 사용하지 않는 방이라면, O(logN)
        if room_number[i] not in used:
            used.add(room_number[i])
            next[room_number[i]] = find(room_number[i] + 1)
            answer.append(room_number[i])
        # 사용중인 방이라면,
        else:
            room = find(next[room_number[i]])
            next[room_number[i]] = room
            used.add(room)
            next[room] = find(room + 1)
            answer.append(room)

    return answer


