import sys


def check_part(seq, n):
    print("----check part----")
    print("seq = ", seq)
    for r in range(1, (n//2)+1):
        print("r = %d" % r)
        print("seq[%d:%d] = " % (n-(2*r), n-r))
        print(seq[n-(2*r):n-r])
        print("seq[%d:%d] = " % (n-r, n))
        print(seq[n-r:n])
        if seq[n-(2*r):n-r] == seq[n-r:n]:
            return False
    return True


def bt(seq, idx):
    global finish
    print("========= idx = %d =========" % idx)
    print("seq = ", seq)
    if len(seq) == m or finish:
        print(seq)
        finish = True
        return

    for num in range(1, 4):
        print("check %d" % num)
        seq.append(num)
        if check_part(seq, len(seq)):
            bt(seq, idx+1)
        seq.pop()


if __name__ == '__main__':
    m = int(sys.stdin.readline().strip())

    finish = False
    bt([], 0)
