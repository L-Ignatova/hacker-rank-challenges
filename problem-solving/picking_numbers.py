# link to problem: https://www.hackerrank.com/challenges/picking-numbers/problem
from collections import Counter


def pickingNumbers(a):
    counted = Counter(a)
    max_subset_size = 0

    for num in a:
        curr_subset_size = counted[num] + (counted[num+1] or 0)
        max_subset_size = curr_subset_size if curr_subset_size > max_subset_size else max_subset_size
    return max_subset_size


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
print(result)