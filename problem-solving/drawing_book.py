# link to problem: https://www.hackerrank.com/challenges/drawing-book/problem
import math


def pageCount(n, p):
    first_half = int(p/2)
    second_half = n/2 - p/2
    if n % 2 == 0:
        return math.ceil(min(first_half, second_half))
    else:
        return int(min(first_half, second_half))


n = int(input().strip())
p = int(input().strip())
print(pageCount(n, p))

