def solution(enroll, referral, seller, amount):
    parent, number, result = {'-': ""}, {'-': 0}, [0 for _ in range(len(enroll)+1)]
    for i in range(len(enroll)):
        parent[enroll[i]] = referral[i]
        number[enroll[i]] = i+1

    for i in range(len(seller)):
        name, profit = seller[i], amount[i] * 100
        result[number[name]] += profit
        while parent[name] != '-':
            if profit == 0:
                break
            profit = int(profit * 0.1)
            result[number[name]] -= profit

            name = parent[name]
            result[number[name]] += profit

        if parent[name] == '-':
            result[number[name]] -= int(profit * 0.1)

    answer = result[1:]
    return answer
