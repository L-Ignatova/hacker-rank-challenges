# link to problem: https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, k, b):
    anna = (sum(bill) - bill[k]) / 2
    if anna == b:
        return 'Bon Appetit'
    else:
        return int(b - anna)


first_multiple_input = input().rstrip().split()
n, k = int(first_multiple_input[0]), int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

print(bonAppetit(bill, k, b))