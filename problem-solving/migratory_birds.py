# link to problem: https://www.hackerrank.com/challenges/migratory-birds/problem

from collections import Counter

def migratoryBirds(arr):
    counter_dict = sorted(Counter(arr).items(), key=lambda x: (-x[1],x[0]))
    return counter_dict[0][0]

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))