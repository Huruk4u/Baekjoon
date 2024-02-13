import sys
input = sys.stdin.readline


def is_exp():
    for i in range(1, len(exp_string)+1):
        if stack[-i] != exp_string[-i]:
            return False
    return True


if __name__ == '__main__':
    string = list(input().strip())
    exp_string = list(input().strip())

    stack = []

    for i in range(len(string)):
        stack.append(string[i])
        # stack의 길이가 폭발 문자열 길이보다 길거나 같다면
        if len(stack) >= len(exp_string):
            if is_exp():
                for _ in range(len(exp_string)):
                    stack.pop()

    if not stack:
        print("FRULA")
    else:
        print("".join(stack))
