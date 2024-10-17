import sys
input = sys.stdin.readline


def typing(used_key):
    global space
    # 스페이스바를 사용하는 경우
    if used_key == ' ':
        if not space:
            return False
        else:
            space -= 1
            return True
    # 영문키를 사용하는 경우
    else:
        used_key = used_key.lower()
        key_idx = ord(used_key) - ord('a')
        if not alpha[key_idx]:
            return False
        else:
            alpha[key_idx] -= 1
            return True


if __name__ == '__main__':
    poet = input().strip()
    space = int(input().strip())
    alpha = list(map(int, input().strip().split()))

    flag = True
    title = [poet[0].upper()]
    if not typing(poet[0]): flag = False   
    prev_key = poet[0].upper()
    # 제목 작성
    for i in range(1, len(poet)):
        if poet[i] != ' ' and poet[i-1] == ' ':
            if poet[i].upper() != prev_key:
                if not typing(poet[i]):
                    flag = False
                    break
            title.append(poet[i].upper())
            prev_key = poet[i].upper()

    # 내용 작성
    prev_key = ''
    for i in range(len(poet)):
        if poet[i] != prev_key:
            if not typing(poet[i]):
                flag = False
                break
        prev_key = poet[i]

    if flag:
        title = ''.join(title)
        print(title)
    else:
        print(-1)
