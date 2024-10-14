import sys
input = sys.stdin.readline


if __name__ == '__main__':
    ipt = input().strip()
    dict_opr = {'c': 26, 'd': 10}
    prev = 'a'
    rtn = 1
    for opr in ipt:
        # 형식이 일치하는 경우
        if opr == prev:
            rtn *= dict_opr[opr] - 1
        else:
            rtn *= dict_opr[opr]
        prev = opr

    print(rtn)
