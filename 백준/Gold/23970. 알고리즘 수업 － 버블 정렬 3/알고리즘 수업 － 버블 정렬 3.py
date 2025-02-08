import sys
input = sys.stdin.readline


# A배열의 정렬 단계를 return한다.
def get_step(state):
    step = 0
    for i in range(N-1, -1, -1):
        if sorted_A[i] == state[i]:
            step += 1
        else:
            return step

    return step


# A배열과 B배열이 같은 지를 검사한다.
def same(a, b):
    for i in range(N):
        if a[i] != b[i]:
            return False
    return True


"""
    bubble sort 0단계.
    step_a가 step_b에 도달할 때까지 bubble sort
"""
def bubble_sort_0(step_b):
    step_a = get_step(A)
    while step_a < step_b:
        for i in range(N - step_a - 1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        # 한 번의 정렬 단계에서 가장 큰 두 개의 수가 정렬될 수 있으므로, step을 매 턴마다 세줘야 한다.
        step_a = get_step(A)


"""
    bubble sort 1단계.
    step_b단계에서 스위칭을 하면서 A배열과 B배열이 같아지는 순간이 있는지를 검사한다.
"""
def bubble_sort_1(step_b):
    if same(A, B):
        return 1
    for i in range(N - step_b - 1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
        if same(A, B):
            return 1
    return 0


if __name__ == '__main__':
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    sorted_A = sorted(A)

    # A의 상태와 B의 상태를 점검한다.
    step_b = get_step(B)
    bubble_sort_0(step_b = step_b) # A의 버블 정렬 단계가 B와 동일해질 때까지 버블정렬


    print(bubble_sort_1(step_b = step_b))
