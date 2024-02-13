import sys


def check_part(seq, n):
    for r in range(1, (n//2)+1):
        if seq[n-(2*r):n-r] == seq[n-r:n]:
            return False
    return True


def bt(seq, idx):
    global finish
    if finish:
        return

    if len(seq) == m:
        print("".join(map(str, seq)))
        finish = True
        return

    for num in range(1, 4):
        seq.append(num)
        if check_part(seq, len(seq)):
            bt(seq, idx+1)
        seq.pop()


if __name__ == '__main__':
    m = int(sys.stdin.readline().strip())

    finish = False
    bt([], 0)
