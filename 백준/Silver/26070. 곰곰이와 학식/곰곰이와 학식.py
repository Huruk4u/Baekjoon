import sys
input = sys.stdin.readline


def eat_gomgom(food):
    global answer
    number_food = min(gomgom[food], ticket[food])
    answer += number_food

    gomgom[food] -= number_food
    ticket[food] -= number_food
    return


def ticket_switching():
    ticket[0], ticket[1], ticket[2] = ticket[2] // 3, ticket[0] // 3, ticket[1] // 3
    return


if __name__ == '__main__':
    gomgom = list(map(int, input().strip().split()))
    ticket = list(map(int, input().strip().split()))
    answer = 0

    for _ in range(3):
        for i in range(3):
            eat_gomgom(i)
        ticket_switching()

    print(answer)
