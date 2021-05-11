# link to problem: https://www.hackerrank.com/challenges/pairs/problem
from itertools import combinations


def pairs(k, arr):
    ll = [abs(comb[0] - comb[1]) for comb in combinations(arr, 2)]
    return ll.count(k)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))

print(pairs(k, arr))