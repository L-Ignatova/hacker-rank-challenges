# link to problem: https://www.hackerrank.com/challenges/electronics-shop/problem


def get_money_spent(keyboards, drives, b):
    total_cost = [-1]
    for k in keyboards:
        for d in drives:
            sum = k + d
            if total_cost[0] < sum <= b:
                total_cost = [sum]
    return max(total_cost)



bnm = input().split()
b = int(bnm[0])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

money_spent = get_money_spent(keyboards, drives, b)
print(money_spent)